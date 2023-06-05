import pygame
import Common

class Shooter:

    #surface & rects
    shooter_rect = pygame.Rect((1000,300),(100,100))

    #function related variables
    dragging = False
    bought = False

    def __init__(self,level,location,set):
        self.level = level
        self.location = location
        self.set = set

    def move(self):
         for events in pygame.event.get():
            if events.type == self.shooter_rect.collidepoint() and pygame.MOUSEBUTTONDOWN and self.set == False:
                self.dragging = True
            if events.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
                self.set == True
            if events.type == pygame.MOUSEMOTION and self.dragging:
                self.shooter_rect.move_ip(events.rel)

    def deploy(self):
        if self.shooter_rect.x <= 900 and Common.money >= 250:
            self.bought = True
            Common.money -= 250

    
    def create(self):
        if self.bought == True:
            self.shooter_rect_d = self.shooter_rect.duplicate()
            self.move()





