import pygame
from helpers import *


# set up the Bomb Diffusion Game

pygame.init()

# make a clock
clock = pygame.time.Clock()

# set a resolution for screen

WIDTH = 700
HEIGHT = 600
# sets the width and height to
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# fill the screen with a white color. Possibility is that screen changes color when time is running out


# Main game loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        screen.fill((255, 255, 255))
        # Update display
        pygame.display.flip()



