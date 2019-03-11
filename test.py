import os,sys
import pygame as pg
import math as math
import piece as piece
import board as board

bg = pg.image.load(os.path.join("images", "Board.png"))
#pawn = pg.image.load(os.path.join("images", "Chess_plt60.png"))
#pawn = pg.transform.scale(pawn,(100,100))

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

pawn = piece.piece("white","pawn")
if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    Screen = pg.display.set_mode((900,900))
    MyClock = pg.time.Clock()
    pg.display.update()
    mx,my = pg.mouse.get_pos()
    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mx,my = pg.mouse.get_pos()
                pawn.pos = gameBoard.findClosestSquare((mx,my))
        Screen.blit(bg, (0,0))    
        Screen.blit(pawn.image,pawn.pos)   
        pg.display.update()
        MyClock.tick(60)
