import pygame
from sys import exit
from Classes import Shooter

money = 0

display = pygame.display.set_mode((1200,800))
map = pygame.image.load(r"C:\Users\emmir\Downloads\TD_Map.jpg").convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif Shooter.deploy():
            Shooter.deploy()

    display.blit(map,(0,0))
    pygame.draw.rect(display,"Blue",Shooter.shooter_rect)
    

    pygame.display.flip()
