import os,sys
import pygame as pg
import math as math

class piece:
    def __init__(self, type, color):
        self.pos = (0,0)
        self.image = pg.image.load(os.path.join("images", imageDict[type+color]))
        self.image = pg.transform.scale(self.image,(100,100))


imageDict = {
    "whitepawn":"Chess_plt60.png",
    "blackpawn":"Chess_pdt60.png",
    "whitebishop": "Chess_blt60.png",
    "blackbishop": "Chess_bdt60.png",
    "whiteking": "Chess_klt60.png",
    "blackking": "Chess_kdt60.png",
    "whiteknight": "Chess_nlt60.png",
    "blackknight": "Chess_ndt60.png",
    "whitequeen": "Chess_qlt60.png",
    "blackqueen": "Chess_qdt60.png",
    "whiterook": "Chess_rlt60.png",
    "blackrook": "Chess_rdt60.png",
}