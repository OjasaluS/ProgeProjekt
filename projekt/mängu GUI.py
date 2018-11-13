import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((640,480))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen.fill(white)
pygame.draw.rect(screen, black, (10,10,620,460), 3)
pygame.draw.rect(screen, black, (11,11, 75,150), 3)
pygame.draw.rect(screen, black, (25,15, 40,30), 3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();
    pygame.display.update()