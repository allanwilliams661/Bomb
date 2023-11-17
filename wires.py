import pygame
import random

class Wires(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, wire_width: int, wire_height: int, color=None, image_path=None) -> None:
        super().__init__()
        self.color = color
        self.image_path = image_path
        self.wire_width = wire_width
        self.wire_height = wire_height
        self.rect = pygame.Rect(x, y, wire_width, wire_height)
        self.make_color()

        if self.image_path:
            self.image = pygame.image.load(self.image_path)
            self.image = pygame.transform.scale(self.image, (self.wire_width, self.wire_height))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)  # Set the top-left corner position

    def randomize_position(self):
        screen_width, screen_height = 800, 600  # Define your screen dimensions here
        max_x = screen_width - self.wire_width  # Calculate the maximum x-coordinate to keep the sprite within the screen
        max_y = screen_height - self.wire_height  # Calculate the maximum y-coordinate

        self.rect.x = random.randint(0, max_x)  # Randomize x-coordinate within the screen bounds
        self.rect.y = random.randint(0, max_y)  # Randomize y-coordinate within the screen bounds

    def make_color(self):
        color_picker = random.randint(1, 4)
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



