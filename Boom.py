import random

import pygame.sprite

from main import *
from wires import *

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, bomb_width: int, bomb_height: int, image_path=None) -> None:
        super().__init__()
        self.original_x = x
        self.original_y = y
        self.rect = pygame.Rect(x, y, bomb_width, bomb_height)
        self.speed_x = random.choice([-2, -1, 1, 2])  # Random initial horizontal speed
        self.speed_y = random.choice([-2, -1, 1, 2])  # Random initial vertical speed

        if image_path:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (bomb_width, bomb_height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.acceleration = 0.01  # Speed increase rate
        self.max_speed = 4  # Maximum speed limit

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Randomly change direction
        if random.randint(0, 100) < 2:
            self.speed_x *= -1
        if random.randint(0, 100) < 2:
            self.speed_y *= -1

        # Gradually increase speed over time
        self.speed_x = min(self.speed_x + self.acceleration, self.max_speed) if self.speed_x > 0 else max(self.speed_x - self.acceleration, -self.max_speed)
        self.speed_y = min(self.speed_y + self.acceleration, self.max_speed) if self.speed_y > 0 else max(self.speed_y - self.acceleration, -self.max_speed)

        # Keep the bomb within screen boundaries
        if self.rect.left < 0 or self.rect.right > 800:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.speed_y *= -1

