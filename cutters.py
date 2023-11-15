
from Main import *

class Cutters(pygame.sprite.Sprite):
    def __init__(self, x, y, cutter_width, cutter_height):
        super().__init__()
        self.rect = pygame.Rect(x,y, cutter_width, cutter_height)
        self.image = pygame.image.load('wire_cut.png')
        # I will only need to change this if the cutter image is too big. Then I would have to use transform.scale
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 6
        # cutters start in the middle of the screen
        self.rect.x = screen.get_width()/2
        self.rect.y = screen.get_width()/2

    def move_cutters(self,keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:  # <800 makes sure it can not go off the screen
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < 600:  # <600 makes sure it can not go off the screen
            self.rect.y += self.speed






