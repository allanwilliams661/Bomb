
from Main import *

class Cutters(pygame.sprite.Sprite):
    def __init__(self, x, y, cutter_width, cutter_height, image):
        super().__init__()
        self.rect = pygame.Rect(x,y, cutter_width, cutter_height)
        self.image = pygame.image.load('wire_cut.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 6
        # cutters start in the middle of the screen
        self.rect.x = screen.get_width()/2
        self.rect.y = screen.get_width()/2



