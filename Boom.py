import random

from main import *
from wires import *

def Bomb_Go_Off():
    bomb_image_path = 'boom_image.png'
    image = pygame.image.load(bomb_image_path)
    image_rect = image.get_rect()
    screen.blit(image, image_rect)


