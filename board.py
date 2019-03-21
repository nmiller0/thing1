import os
import sys
import pygame as pg
import math as math
import piece as piece


class board:
    def __init__(self):
        self.board = []
        startx = 42.5
        starty = 770  # (900-42.5)

        for x in range(8):
            row = []
            for i in range(8):
                row.append((startx, starty))
                startx += 102.5
            self.board.append(row)
            startx = 42.5
            starty -= 102.5
        
        self.setupBoard()

    def findClosestSquare(self, pos):
        closestPoint = (0, 0)
        closestPointDist = 900
        for row in self.board:
            for r in row:
                rDist = distance(pos, (r[0]+50, r[1]+50))
                if(rDist < closestPointDist):
                    closestPoint = r
                    closestPointDist = rDist
        return closestPoint
    def findPieceAt(self, pos):
        for p in self.pieces:
            if(pos == p.pos):
                return p
        
    def setupBoard(self):
        self.pieces = []
        for p in self.board[1]:
            self.pieces.append(piece.piece("pawn","black",p))

        for p in self.board[6]:
            self.pieces.append(piece.piece("pawn","white",p))

    def movePiece(self, a, b):
        ax = sqDict[a[0]]
        ay = int(a[1])-1
        bx = sqDict[b[0]]
        by = int(b[1])-1
        newPos = self.board[bx][by]
        p = self.findPieceAt(self.board[ax][ay])
        p.pos = newPos




def distance(p, q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)


sqDict = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}
