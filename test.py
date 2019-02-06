import os,sys
import pygame as pg

bg = pg.image.load(os.path.join("images", "Board.png"))
pawn = pg.image.load(os.path.join("images", "pawn.png"))
pawn = pg.transform.scale(pawn,(100,100))

x = 0
y = 0
r = 0

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
        Screen.blit(bg, (0,0))        
        Screen.blit(pawn,(mx-50,my-50))
        pg.display.update()
        MyClock.tick(60)
