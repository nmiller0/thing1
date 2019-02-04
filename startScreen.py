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

black = (0,0,0)
white = (255,255,255)


x =  (display_width * 0.40)
y = (display_height * 0.8)

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)
    gameDisplay.fill(white)
    startButton(x,y)
    pygame.display.update()
    clock.tick(60)

