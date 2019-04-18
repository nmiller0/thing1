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
        self.pieces = []
        for x in range(8):
            row = []
            for i in range(8):
                row.append((startx, starty))
                startx += 102.5
            self.board.append(row)
            startx = 42.5
            starty -= 102.5
        
        #self.setupBoard()
    def convertPositionToSquare(self, pos):
        coords = ("a", "1")
        i = 0
        x = 0
        print(len(self.board))
        while i < len(self.board):
            while x < len(self.board[i]):
                sq = self.board[i][x]
                if(sq == pos):
                    print("FOUND")
                    coords = (x, i)
                    print(oDict[coords[0]] + str(i+1))
                    return oDict[coords[0]] + str(i+1);
                x += 1
            x = 0;
            i += 1
        
        


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
            self.pieces.append(piece.piece("pawn","white",p))

        for p in self.board[6]:
            self.pieces.append(piece.piece("pawn","black",p))
        
        self.pieces.append(piece.piece("rook","white",self.board[0][0]))
        self.pieces.append(piece.piece("knight","white",self.board[0][1]))
        self.pieces.append(piece.piece("bishop","white",self.board[0][2]))
        self.pieces.append(piece.piece("queen","white",self.board[0][4]))
        self.pieces.append(piece.piece("king","white",self.board[0][3]))
        self.pieces.append(piece.piece("bishop","white",self.board[0][5]))
        self.pieces.append(piece.piece("knight","white",self.board[0][6]))
        self.pieces.append(piece.piece("rook","white",self.board[0][7]))

        self.pieces.append(piece.piece("rook","black",self.board[7][0]))
        self.pieces.append(piece.piece("knight","black",self.board[7][1]))
        self.pieces.append(piece.piece("bishop","black",self.board[7][2]))
        self.pieces.append(piece.piece("queen","black",self.board[7][4]))
        self.pieces.append(piece.piece("king","black",self.board[7][3]))
        self.pieces.append(piece.piece("bishop","black",self.board[7][5]))
        self.pieces.append(piece.piece("knight","black",self.board[7][6]))
        self.pieces.append(piece.piece("rook","black",self.board[7][7]))

    def movePiece(self, a, b):
        ax = int(a[1])-1
        ay = sqDict[a[0]]
        bx = int(b[1])-1
        by = sqDict[b[0]]
        newPos = self.board[bx][by]
        p = self.findPieceAt(self.board[ax][ay])
        p.pos = newPos
        return newPos

    def convertSquareToPos(self, a):
        ax = int(a[1])-1
        ay = sqDict[a[0]]
        newPos = self.board[ax][ay]
        return newPos

    def getStateFromPc(self, state):
        self.pieces = [];
        x = 0
        y = 7
        for c in state:
            if(c.islower()):
                if(c == "r"):
                    self.pieces.append(piece.piece("rook","black",self.board[y][x]))
                if c == "n":
                    self.pieces.append(piece.piece("knight","black",self.board[y][x]))
                if c == "q":
                    self.pieces.append(piece.piece("queen","black",self.board[y][x]))
                if c == "k":
                    self.pieces.append(piece.piece("king","black",self.board[y][x]))
                if c == "b":
                    self.pieces.append(piece.piece("bishop","black",self.board[y][x]))
                if c == "q":
                    self.pieces.append(piece.piece("queen","black",self.board[y][x]))
                if c == "p":
                    self.pieces.append(piece.piece("pawn","black",self.board[y][x]))
            else:
                nc = c.lower()
                if(nc == "r"):
                    self.pieces.append(piece.piece("rook","white",self.board[y][x]))
                if nc == "n":
                    self.pieces.append(piece.piece("knight","white",self.board[y][x]))
                if nc == "q":
                    self.pieces.append(piece.piece("queen","white",self.board[y][x]))
                if nc == "k":
                    self.pieces.append(piece.piece("king","white",self.board[y][x]))
                if nc == "b":
                    self.pieces.append(piece.piece("bishop","white",self.board[y][x]))
                if nc == "q":
                    self.pieces.append(piece.piece("queen","white",self.board[y][x]))
                if nc == "p":
                    self.pieces.append(piece.piece("pawn","white",self.board[y][x]))

            if( c != " " and not c.isspace()):
                x += 1
                if x > 7:
                    y -= 1
                    x = 0

            
def distance(p, q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

oDict = {
    0 : "a",
    1 : "b",
    2 : "c",
    3 : "d",
    4 : "e",
    5 : "f",
    6 : "g",
    7 : "h"
}

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
