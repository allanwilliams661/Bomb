import pygame
import sys
from pygame.sprite import Group

class Cutter(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, cutter_width: int, cutter_height: int, image_path=None) -> None:
        super().__init__()
        self.rect = pygame.Rect(x, y, cutter_width, cutter_height)
        self.speed = 5

        if image_path:
            # Load image if path is provided
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (cutter_width, cutter_height))
        else:
            self.image = pygame.Surface((cutter_width, cutter_height))
            self.image.fill((255, 0, 0))  # Red colored surface if no image is provided

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, keys: pygame.key.get_pressed) -> None:
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:  # Adjust 800 based on your screen width
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < 600:  # Adjust 600 based on your screen height
            self.rect.y += self.speed
    def snip(self,keys: pygame.key.get_pressed) -> None:
        if








