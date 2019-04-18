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



def listen(x):
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.pause_threshold = x
		r.non_speaking_duration = x
		r.adjust_for_ambient_noise(source, duration = x)
		audio = r.listen(source)
	try:
		command = r.recognize_google(audio)
	#Loops until something is understood
	except sr.UnknownValueError:
		command = listen(x)
	return command

commandQueue = queue.Queue()

def get_Command():
        while True:
                print("Say 'chess.'")
                keycheck = listen(0.1)
                keyphrase = keycheck.split()
                #change test word here 
                if "chess" in keyphrase:
                        while True:
                                print("Say a move.")
                                command = listen(.5)
                                moveList = ['A1','A2','A3','A4','A5','A6','A7','A8',
                                            'B1','B2','B3','B4','B5','B6','B7','B8',
                                            'C1','C2','C3','C4','C5','C6','C7','C8',
                                            'D1','D2','D3','D4','D5','D6','D7','D8',
                                            'E1','E2','E3','E4','E5','E6','E7','E8',
                                            'F1','F2','F3','F4','F5','F6','F7','F8',
                                            'G1','G2','G3','G4','G5','G6','G7','G8',
                                            'H1','H2','H3','H4','H5','H6','H7','H8']
                                print("I heard: ", command)
                                command1 = command.split()
                                if command1[0] in moveList and len(command1) == 2:
                                        if command1[1] in moveList:
                                                print("Is that correct?")
                                                keycheck1 = listen(0.5)
                                                keyphrase1 = keycheck1.split()
                                                if "yes" in keyphrase1:
                                                        print("Move has been made!")
                                                        commandQueue.put(command)
                                                        return command

def parseCommand(command):
    splitCommand = command.lower().split()
    return splitCommand


def main():
    command = get_Command()
    parseCommand(command)


bg = pg.image.load(os.path.join("images", "Board.png"))

# create the python-chess version of the board, which is for game-state
pcBoard = chess.Board()
# create our version of the board, which is mainly for graphics interface stuff
gameBoard = board.board()
gameBoard.getStateFromPc(str(pcBoard))
if __name__ == "__main__":

    # setup stuff
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

    # loop while game is running
    while 1:
        # check if voice input is over
        if not voiceThread.is_alive():
            voiceThread.join()
            foundCommand = parseCommand(commandQueue.get())
            print("COMMAND RETURNED: " +
                  foundCommand[0] + " " + foundCommand[1])
            move = chess.Move.from_uci(foundCommand[0]+foundCommand[1])
                # check if move was legal. if not, move the piece back
            if move in pcBoard.legal_moves:
                pcBoard.push(move)
            gameBoard.getStateFromPc(str(pcBoard))
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
                    gameBoard.getStateFromPc(str(pcBoard))
                else:
                    piece.pos = gameBoard.convertSquareToPos(orgCoord)

        validMoves = []

        # if the mouse button is down, update piece position (drag)
        # then iterate to find all valid moves for that square
        if mouseDown:
            piece.pos = (mx-50, my-50)
            for i in range(8):
                for x in range(8):
                    # the input to the move.from_uci is the origin square (like "a1"),
                    # plus the indices of the 2d array of squares but converted to a string as well
                    if chess.Move.from_uci(orgCoord+board.oDict[i]+str(x+1)) in pcBoard.legal_moves:
                        validMoves.append((orgCoord+board.oDict[i]+str(x+1)))

        # draw the background
        # also, drawing is in a particular order
        Screen.blit(bg, (0, 0))

        # draw green squares on all valid move spots
        for sq in validMoves:
            x = gameBoard.convertSquareToPos(str(sq[2]+sq[3]))
            left = x[0]+50
            top = x[1]+42
            width = 102.5
            height = 102.5
            #pygame.draw.circle(screen, color, (x,y), radius, thickness)
            pg.draw.circle(Screen, [0, 255, 0], (int(left), int(top)), 50 ,0)

        # draw all game pieces
        for p in gameBoard.pieces:
            Screen.blit(p.image, p.pos)

        pg.display.update()
        MyClock.tick(60)
