import os,sys
import pygame as pg
import math as math
class board:
    def __init__(self):
        self.board = []
        startx = 42.5
        starty = 770 #(900-42.5)

        for x in range(8):
            row = []
            for i in range(8):
                row.append((startx , starty))
                startx += 102.5
            self.board.append(row)
            startx = 42.5
            starty -= 102.5
    def findClosestSquare(self,pos):
        closestPoint = (0,0)
        closestPointDist = 900
        for row in self.board:
            for r in row:
                rDist = distance(pos,(r[0]+50,r[1]+50))
                if(rDist < closestPointDist):
                    closestPoint = r
                    closestPointDist = rDist
        return closestPoint


def distance(p,q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

sqDict = {
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7
}