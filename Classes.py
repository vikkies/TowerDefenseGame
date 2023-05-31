import pygame
from Main import money

class Shooter:

    #surface & rects
    shooter_rect = pygame.Rect((1000,300),(100,100))

    #function related variables
    dragging = False
    bought = False

    def __init__(self,level,location):
        self.level = level
        self.location = location

    @classmethod
    def deploy(self,money):
        for events in pygame.event.get():
            if self.shooter_rect.collidepoint() and pygame.MOUSEBUTTONDOWN:
                self.dragging = True
            elif pygame.MOUSEBUTTONUP:
                self.dragging = False
            elif pygame.MOUSEMOTION and self.dragging:
                self.shooter_rect.move_ip(events.rel)
            elif self.shooter_rect.x <= 900 and money >= 250:
                self.bought = True

    
    def create(self):
        if self.bought == True:
            self.shooter_rect.duplicate()





