import os
import sys
import pygame as pg
import math as math
import piece as piece
import board as board
import threading
import queue
import speech_recognition as sr
import chess

pcBoard = chess.Board()

def listen(x):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = x
        r.non_speaking_duration = x
        r.adjust_for_ambient_noise(source, duration=x)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
    # Loops until something is understood
    except sr.UnknownValueError:
        command = listen(x)
    return command


commandQueue = queue.Queue()


def get_Command():
    while True:
        print("Say 'chess.'")
        keycheck = listen(0.1)
        keyphrase = keycheck.split()
        # change test word here
        if "chess" in keyphrase:
            print("Say a move.")
            command = listen(.5)
            print("I heard: ", command)
            print("Is that correct?")
            keycheck1 = listen(0.5)
            keyphrase1 = keycheck1.split()
            if "yes" in keyphrase1:
                print("Move has been made!")
                commandQueue.put(command)
                return command
                break


def parseCommand(command):
    splitCommand = command.lower().split()
    return splitCommand


def main():
    command = get_Command()
    parseCommand(command)


bg = pg.image.load(os.path.join("images", "Board.png"))

gameBoard = board.board()

pawn = pg.image.load(os.path.join("images", "pawn.png"))
vt = pg.image.load(os.path.join("images", "test.png"))
pawn = pg.transform.scale(pawn, (100, 100))

x = 0
y = 0
r = 0

pawn = piece.piece("pawn", "white")
if __name__ == "__main__":

    #setup stuff
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    Screen = pg.display.set_mode((900, 900))
    MyClock = pg.time.Clock()
    pg.display.update()
    mx, my = pg.mouse.get_pos()
    piece = 0
    mouseDown = False
    voiceThread = threading.Thread(target=get_Command)
    voiceThread.start()

    #loop while game is running
    while 1:
        #check if voice input is over
        if not voiceThread.is_alive():
            voiceThread.join()
            foundCommand = parseCommand(commandQueue.get())
            print("COMMAND RETURNED: " +
                  foundCommand[0] + " " + foundCommand[1])
            gameBoard.movePiece(foundCommand[0], foundCommand[2])
            voiceThread = threading.Thread(target=get_Command)
            voiceThread.start()
        mx, my = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouseDown = True
                sqClicked = gameBoard.findClosestSquare((mx, my))
                piece = gameBoard.findPieceAt(sqClicked)
                orgCoord = gameBoard.convertPositionToSquare(sqClicked)
            elif event.type == pg.MOUSEBUTTONUP:
                mouseDown = False
                
                # snap piece to closest square
                piece.pos = gameBoard.findClosestSquare((mx, my))
                newCoord = gameBoard.convertPositionToSquare(piece.pos)
                move = chess.Move.from_uci(orgCoord+newCoord)

                # check if move was legal. if not, move the piece back
                if move in pcBoard.legal_moves:
                    pcBoard.push(move)
                else:
                    piece.pos = gameBoard.convertSquareToPos(orgCoord)

                # check to see if any pieces have been taken and remove them
                for p in gameBoard.pieces:
                    if p.pos == piece.pos and p != piece:
                        gameBoard.pieces.remove(p)
                        print(pcBoard)
                        break

        validMoves = []

        #if the mouse button is down, update piece position (drag)
        #then iterate to find all valid moves for that square
        if mouseDown:
            piece.pos = (mx-50, my-50)
            for i in range(8):
                for x in range(8):
                    if chess.Move.from_uci(orgCoord+board.oDict[i]+str(x+1)) in pcBoard.legal_moves:
                        validMoves.append((orgCoord+board.oDict[i]+str(x+1)))
            
        #draw the background
        Screen.blit(bg, (0, 0))
        
        #draw green squares on all valid move spots
        for sq in validMoves:
                print(str(sq[2]+sq[3]))
                x = gameBoard.convertSquareToPos(str(sq[2]+sq[3])) 
                left= x[0]
                top= x[1]
                width=95
                height=95
                pg.draw.rect(Screen, [0, 255, 0], [left, top, width, height], 0)
        
        #draw all game pieces
        for p in gameBoard.pieces:
            Screen.blit(p.image, p.pos)
        pg.display.update()
        MyClock.tick(60)
