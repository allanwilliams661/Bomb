import pygame.sprite

from cutter_sprite import *
from wires import *
from timer import *
from Boom import *
from score import *


def main() -> None:
    # Initialize Pygame
    pygame.init()
    # Initialize the sound mixer
    pygame.mixer.init()

    # Set up display
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Diffuse the Bomb")

    # Define sprite Groups.
    wire_sprites = pygame.sprite.Group()
    cutter_sprite = pygame.sprite.Group()
    bomb_sprite = pygame.sprite.Group()
    score_sprite = pygame.sprite.Group()
    # Create cutter instance with image
    score_font = pygame.font.Font(None, 36)
    scoreboard = Scoreboard(10, 10, score_font)
    cutters = Cutter(50, 50, 50, 50, image_path="wire_cut.png")
    bomb_instance1 = Bomb(100, 50, 50, 50, image_path='tnt_bomb.png')
    bomb_instance2 = Bomb(100, 150, 50, 50, image_path='tnt_bomb.png')
    bomb_instance3 = Bomb(100, 250, 50, 50, image_path='tnt_bomb.png')
    bomb_instance4 = Bomb(100, 350, 50, 50, image_path='tnt_bomb.png')
    bomb_instance5 = Bomb(100, 450, 50, 50, image_path='tnt_bomb.png')
    bomb_instance6 = Bomb(100, 550, 50, 50, image_path='tnt_bomb.png')

    timer_sprite = Timer(SCREEN_WIDTH / 2, 250, 53, 50)

    # Make wire sprite instances
    wire_instance1 = Wires(100, 100, 200, 10)
    wire_instance2 = Wires(300, 200, 150, 8)
    wire_instance3 = Wires(500, 300, 180, 12)
    wire_instance4 = Wires(200, 400, 220, 6)
    wire_instance5 = Wires(600, 150, 170, 9)
    wire_instance6 = Wires(400, 500, 190, 7)
    wire_instance7 = Wires(150, 250, 210, 11)
    wire_instance8 = Wires(350, 450, 160, 5)
    wire_instance9 = Wires(700, 350, 230, 10)
    wire_instance10 = Wires(250, 150, 175, 8)
    cutter_sprite.add(cutters)
    wire_sprites.add(wire_instance1, wire_instance2, wire_instance3, wire_instance4, wire_instance5,wire_instance6,wire_instance7,wire_instance8,wire_instance9,wire_instance10)

    bomb_sprite.add(bomb_instance1,bomb_instance2,bomb_instance3,bomb_instance4,bomb_instance5,bomb_instance6)
    score_sprite.add(scoreboard, timer_sprite)
    wire_list = list(wire_sprites.sprites())



    wires_cut = 0

    # Main game loop
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Check for collisions between cutter and wires when space bar is pressed
                collisions_wire_cutter = pygame.sprite.spritecollide(cutters, wire_sprites, False)
                for wire in collisions_wire_cutter:
                    wires_cut = wires_cut + 1
                    wire.kill()
                    scoreboard.increase_score()
                    scoreboard.update_score()
            if pygame.sprite.spritecollide(cutters, bomb_sprite, False):
                scoreboard.decrease_score()
                scoreboard.update_score()
            if scoreboard.score == -1:
                #make health sprite with 3 lives. Kill one of the sprites
            elif scoreboard.score == -2:
                #kill one more live sprite
            elif scoreboard.score == -3:
                #kill last life and have bomb go off noise





        # Get the keys that are currently pressed. Could be redundant**
        keys = pygame.key.get_pressed()
        # Move the cutter based on the arrow keys


        timer_sprite.update_timer()
        cutters.update(keys)
        cutters.cut(keys)
        bomb_sprite.update()
        # Fill the screen with a white color
        screen.fill((255, 255, 255))
        # Draw cutter sprite
        cutter_sprite.draw(screen)
        # Draw wire sprites
        bomb_sprite.draw(screen)
        wire_sprites.draw(screen)
        score_sprite.draw(screen)
        score_sprite.update()


        # Update the display
        pygame.display.flip()


        # Set the frame rate
        clock.tick(30)


if __name__ == "__main__":
    main()
