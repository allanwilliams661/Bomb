import random

import pygame.sprite

from main import *
from wires import *

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, bomb_width: int, bomb_height: int, image_path=None) -> None:
        super().__init__()
        self.original_x = x  # Store the original x position
        self.rect = pygame.Rect(x, y, bomb_width, bomb_height)

        if image_path:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (bomb_width, bomb_height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 3  # Adjust the speed as needed

    def update(self):
        # Move the bomb horizontally
        self.rect.x += self.speed

        # If the bomb goes off the screen
        if self.rect.right > 800:
            self.rect.x = -self.rect.width  # Reset bomb's position to the left side

        # If you want to bring the bomb back to the original spot when it goes off the screen
        if self.rect.left < -self.rect.width:
            self.rect.x = self.original_x

