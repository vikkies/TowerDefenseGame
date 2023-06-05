import pygame
from sys import exit
from Classes import Shooter
import Images

display = pygame.display.set_mode((1200,800))
map = Images.map.convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if Shooter.deploy():
            Shooter.deploy()


    display.blit(map,(0,0))
    pygame.draw.rect(display,"Blue",Shooter.shooter_rect)
    

    pygame.display.flip()
