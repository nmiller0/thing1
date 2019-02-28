import os,sys
import pygame as pg

import speech_recognition as sr

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

def get_Command():
        while True:
                print("Say 'chess.'")
                keycheck = listen(0.1)
                keyphrase = keycheck.split()
                #change test word here 
                if "chess" in keyphrase:
                        print("Say a move.")
                        command = listen(.5)
                        print("I heard: ", command)
                        print("Is that correct?")
                        keycheck1 = listen(0.5)
                        keyphrase1 = keycheck1.split()
                        if "yes" in keyphrase1:
                                print("Move has been made!")
                                return command
                                break
def parseCommand(command):
    splitCommand = command.lower().split()
    print(splitCommand)

def main():
        command = get_Command()
        parseCommand(command)


bg = pg.image.load(os.path.join("images", "Board.png"))
pawn = pg.image.load(os.path.join("images", "pawn.png"))
vt = pg.image.load(os.path.join("images", "test.png"))
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
        main()
        Screen.blit(vt, (450,450))
        MyClock.tick(60)
