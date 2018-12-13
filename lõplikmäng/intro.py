import time
import pygame

def intro():    
    pygame.init()

    laius = 1000
    kõrgus = 750

    must = (0,0,0)
    valge = (255,255,255)
    punane = (255,0,0)


    gameDisplay = pygame.display.set_mode((laius, kõrgus))
    pygame.display.set_caption("Tekstipõhine mäng")
    clock = pygame.time.Clock()

    pilt1 = pygame.image.load("pilt1.jpg")

    def pilt(a,b):
        gameDisplay.blit(pilt1,(a,b))

    x = (laius*0.0001)
    y = (kõrgus*0.0001)

    error = False

    while not error:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                error = True
        gameDisplay.fill(valge)
        pilt(x,y)
        
        pygame.display.update()
        clock.tick(60)
        time.sleep(2)
        error = True

    pygame.quit()
