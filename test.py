import os,sys
import pygame as pg
import math as math
import piece as piece
import board as board

bg = pg.image.load(os.path.join("images", "Board.png"))

gameBoard = board.board()

def findClosestSquare(pos,board):
    closestPoint = (0,0)
    closestPointDist = 900
    for row in board:
        for r in row:
            rDist = distance(pos,(r[0]+50,r[1]+50))
            if(rDist < closestPointDist):
                closestPoint = r
                closestPointDist = rDist
    return closestPoint
            
def distance(p,q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

x = 0
y = 0
r = 0

pawn = piece.piece("pawn","white")
if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    Screen = pg.display.set_mode((900,900))
    MyClock = pg.time.Clock()
    pg.display.update()
    mx,my = pg.mouse.get_pos()
    piece = 0;
    mouseDown = False
    while 1:
        mx,my = pg.mouse.get_pos()
        for event in pg.event.get():
            print(event)
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouseDown = True
                sqClicked = gameBoard.findClosestSquare((mx,my))
                piece = gameBoard.findPieceAt(sqClicked)
            elif event.type == pg.MOUSEBUTTONUP:
                mouseDown = False
                piece.pos = gameBoard.findClosestSquare((mx,my))

        if(mouseDown):
                piece.pos = (mx-50,my-50)

        Screen.blit(bg, (0,0))  
        for p in gameBoard.pieces:  
            Screen.blit(p.image,p.pos)   
        pg.display.update()
        MyClock.tick(60)
