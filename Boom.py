import random

from main import *
from wires import *

def set_correct_wire():
    correct_wire = random.randint(1, 4)

    if correct_wire == 1:
        wire_color = 'red'
    elif correct_wire == 2:
        wire_color = 'blue'
    elif correct_wire == 3:
        wire_color = 'green_yellow'
    elif correct_wire == 4:
        wire_color = 'pink'
    return wire_color
def Bomb_Go_Off():
