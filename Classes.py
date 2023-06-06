import pygame
import Common


class Buttons:

    #surface & rects
    shooter_rect = pygame.Rect((1000,300),(100,100))

    #Buying and placement related variables
    bought = False
    dragging = False
    ready_to_buy = True

    def __init__(self):
        pass

    def purchase():
        if Common.money >= 250 and Buttons.shooter_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            Buttons.bought = True
            Common.money -= 250
            Buttons.ready_to_buy = False 



class Shooter:

    #function related variables
    dragging = False
    shooter_num = 1

    def __init__(self,placed):
        self.placed = placed

    def create(self):
        self.shooter  = Shooter

    def place_rights(self):
        if Buttons.bought == True and Buttons.shooter_rect.collidepoint(pygame.mouse.get_pos()) and pygame.MOUSEBUTTONDOWN:
            self.shooter_rect_c = Buttons.shooter_rect.copy()
            self.dragging = True

    def moving(self):
            if self.dragging:
                self.shooter_rect_c.move_ip(pygame.mouse.get_pos())
            if pygame.MOUSEBUTTONUP:
                self.dragging = False





