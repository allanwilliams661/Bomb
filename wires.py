import pygame
import random

class Wires(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, wire_width: int, wire_height: int, color = None, image_path=None) -> None:
        super().__init__()
        self.rect = pygame.Rect(x, y, wire_width, wire_height)
        self.color = color
        self.image_path = image_path
        self.make_color()
        if image_path:
            # Defines the image path
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (wire_width, wire_height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



    def make_color(self):
        color_picker = random.randint(0,4)
        if color_picker == 1:
            self.color = 'red'
            self.image_path = 'red_wire.PNG'
        elif color_picker == 2:
            self.color = 'blue'
            self.image_path = 'blue_wire.PNG'
        elif color_picker == 3:
            self.color = 'green_yellow'
            self.image_path = 'green_yellow_wire.PNG'
        elif color_picker == 4:
            self.color = 'pink'
            self.image_path = 'pink_wire.PNG'
        return self.color


