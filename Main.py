import pygame
from sys import exit
import Classes
import Images

display = pygame.display.set_mode((1200,800))
map = Images.map.convert()

purchase_wait_time = pygame.event.custom_type()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == purchase_wait_time:
            Classes.Buttons.ready_to_buy = True

    #functions the player can "call"
    if Classes.Buttons.ready_to_buy:
        Classes.Buttons.purchase()
        pygame.time.set_timer(purchase_wait_time, 500)

        

    display.blit(map,(0,0))
    pygame.draw.rect(display,"Blue",Classes.Buttons.shooter_rect)
    pygame.draw.rect(display,"Blue",Classes.Shooter.shooter_rect_c)
    

    pygame.display.flip()

