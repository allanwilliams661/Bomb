
from Main import *

class Cutters(pygame.sprite.Sprite):
    def __init__(self, x, y, cutter_width, cutter_height, image):
        super().__init__()
        self.rect = pygame.Rect(x,y, cutter_width, cutter_height)
        self.image = pygame.image.load('wire_cut.png')
        self.image = pygame.transform.scale(self.image,0.2)
        self.rect = self.image.get_rect()
        # cutters start in the middle of the screen
        self.rect.x = screen.get_width()/2
        self.rect.y = screen.get_width()/2



