import pygame

pygame.init()
display_width = 900
display_height = 900
button_width = 200
button_height = 100
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('thing1: voice chess')
clock = pygame.time.Clock()        

blue = (66, 134, 244)
green = (25, 122, 46)
black = (0,0,0)
white = (255,255,255)

def textObjects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def titleDisplay(text):
    largeText = pygame.font.Font('freesansbold.ttf',32)
    TextSurf, TextRect = textObjects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)


x =  (display_width * 0.40)
y = (display_height * 0.5)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("freesansbold.ttf",24)
    textSurf, textRect = textObjects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def singlePlayerMenu():
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            print(event)
        gameDisplay.fill(white)
        titleDisplay("Select which color you'd like to play")
        button("Start as Black", x,y,button_width,button_height,blue,green)
        button("Start as White", x,y+150,button_width,button_height,blue,green)
        button("Back", x,y+300,button_width,button_height,blue,green, __main__)
        pygame.display.update()
        clock.tick(60)

def __main__():
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            print(event)

        gameDisplay.fill(white)
        titleDisplay("thing1: futuristic voice chess from the future")
        button("Play Single Player", x,y,button_width,button_height,blue,green, singlePlayerMenu)
        button("Quit", x,y+150,button_width,button_height,blue,green, exit)
        pygame.display.update()
        clock.tick(60)

__main__();