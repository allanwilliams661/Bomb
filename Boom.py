import random

import pygame.sprite

from main import *
from wires import *

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, bomb_width: int, bomb_height: int, image_path=None) -> None:
        super().__init__()
        self.rect = pygame.Rect(x, y, bomb_width, bomb_height)



        if image_path:
            # Defines the image path
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (bomb_width, bomb_height))

        # Get/Define the rect and pos of bomb sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

