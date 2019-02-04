import pygame

pygame.init()
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('thing1: voice chess')
imgStartButton = pygame.image.load('./assets/ui/blue_button00.png')

clock = pygame.time.Clock()
def startButton(x,y):
    gameDisplay.blit(imgStartButton,(x,y))
    largeText = pygame.font.Font('freesansbold.ttf',32)
    TextSurf, TextRect = textObjects("Start", largeText)
    TextRect.center = (x+(display_width/9),y+(display_height/20))
    gameDisplay.blit(TextSurf, TextRect)          

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
y = (display_height * 0.8)

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    gameDisplay.fill(white)
    titleDisplay("thing1: futuristic voice chess from the future")
    startButton(x,y)
    pygame.display.update()
    clock.tick(60)

