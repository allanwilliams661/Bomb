import pygame.sprite

from cutter_sprite import *
from wires import *
from timer import *
from Boom import *
from score import *
from clock_sprite import *
from Menu import *




def main() -> None:
    # Initialize Pygame
    pygame.init()
    # Initialize the sound mixer
    pygame.mixer.init()

    # Set up display
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pygame.image.load('game background.png')
    boom_background = pygame.image.load('boom_image.png')
    pygame.display.set_caption("Diffuse the Bomb")

    # Define sprite Groups.
    wire_sprites = pygame.sprite.Group()
    cutter_sprite = pygame.sprite.Group()
    bomb_sprite = pygame.sprite.Group()
    score_sprite = pygame.sprite.Group()
    clock_power_up_group = pygame.sprite.Group()
    ###################################################################################################################
    # Set my score font
    score_font = pygame.font.SysFont('Arial', 36)

    # Create each instance of the bomb, wire, cutter, timer, and scoreboard sprite.
    scoreboard = Scoreboard(10, 10, score_font)
    cutters1 = Cutter(500, 200, 50, 50, image_path='wire_cut.png')


    bomb_instance1 = Bomb(100, 50, 50, 50, image_path='tnt_bomb.png')
    bomb_instance2 = Bomb(100, 150, 50, 50, image_path='tnt_bomb.png')
    bomb_instance3 = Bomb(100, 250, 50, 50, image_path='tnt_bomb.png')
    bomb_instance4 = Bomb(100, 350, 50, 50, image_path='tnt_bomb.png')
    bomb_instance5 = Bomb(100, 450, 50, 50, image_path='tnt_bomb.png')
    bomb_instance6 = Bomb(100, 550, 50, 50, image_path='tnt_bomb.png')
    # Make timer sprite.

    timer_sprite = Timer(SCREEN_WIDTH / 2, 50, 53, 50)

    # Make wire sprite instances
    wire_instance1 = Wires(100, 100, 200, 10)
    wire_instance2 = Wires(300, 200, 150, 8)
    wire_instance3 = Wires(500, 300, 180, 12)
    wire_instance4 = Wires(200, 400, 220, 6)
    wire_instance5 = Wires(600, 150, 170, 9)
    wire_instance6 = Wires(400, 500, 190, 7)
    wire_instance7 = Wires(150, 250, 210, 11)
    wire_instance8 = Wires(350, 450, 160, 5)
    wire_instance9 = Wires(500, 350, 230, 10)
    wire_instance10 = Wires(250, 150, 175, 8)

    # Make clock power up sprite

    clock_power_up_instance = clock_power_up(200,200,60,48,'clock_power.PNG')

    # Add each sprite to their sprite group

    cutter_sprite.add(cutters1)

    wire_sprites.add(wire_instance1, wire_instance2, wire_instance3, wire_instance4, wire_instance5,wire_instance6,wire_instance7,wire_instance8,wire_instance9,wire_instance10)

    bomb_sprite.add(bomb_instance1,bomb_instance2,bomb_instance3,bomb_instance4,bomb_instance5,bomb_instance6)

    score_sprite.add(scoreboard, timer_sprite)

    clock_power_up_group.add(clock_power_up_instance)


######################################################################################################################################################################################################



    # Inisialize the number of wires cut.
    wires_cut = 0


    # Main game loop

    # Set clock ticks and frame rate

    clock = pygame.time.Clock()
    fr = 30
    # Make background music
    game_music = pygame.mixer.Sound('Death-Preview.mp3')
    game_music.play()
    while 1:

        for event in pygame.event.get():

            # Will close game if closed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



             # Gets key data to see if you choose to cut a wire
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Check for collisions between cutter and wires when space bar is pressed
                collisions_wire_cutter = pygame.sprite.spritecollide(cutters1, wire_sprites, False)



                # For loop that 'cuts' the wire kills sprite. Makes score go up. Updates score board.
                for wire in collisions_wire_cutter:
                    wires_cut = wires_cut + 1
                    wire.kill()
                    scoreboard.increase_score()
                    scoreboard.update_score()
            # Sets win conditions
            if wires_cut == 10:
                bomb_instance1.kill()
                bomb_instance2.kill()
                bomb_instance3.kill()
                bomb_instance4.kill()
                bomb_instance5.kill()
                bomb_instance6.kill()
                font = pygame.font.Font('NovaSquare-Regular.ttf', 36)
                win_text = font.render("You Win", True, (153, 122, 0))
                win_text_rect = win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                screen.blit(win_text, win_text_rect)
                scoreboard.you_win()
                pygame.display.flip()

            # Have bomb go off if time gets to 0
            if timer_sprite.seconds == 0 and wires_cut < 10:
                boom_sound = pygame.mixer.Sound('boom.wav')
                boom_sound.play()
                scoreboard.reset_score()
                scoreboard.update_score()
                bomb_instance1.kill()
                bomb_instance2.kill()
                bomb_instance3.kill()
                bomb_instance4.kill()
                bomb_instance5.kill()
                bomb_instance6.kill()
                timer_sprite.reset_time()
                cutters1.bomb_boom()
                scoreboard.you_lose()









            # Will look to see if the cutters hit the bomb sprites. If it does then the score will go down. If you go to -3 the bomb exploes hence the noise.
            if pygame.sprite.spritecollide(cutters1, bomb_sprite, False):
                scoreboard.decrease_score()
                scoreboard.update_score()
            # Make the cutter sprite weak if you get close to detonating the bomb
            if scoreboard.score <= -1:
                cutters1.weak()
                cutter_sprite.draw(screen)
            elif scoreboard.score > -1:
                cutters1.strong()
                cutter_sprite.draw(screen)








            # Detonate the bomb if you lose enough lives.
            if scoreboard.score <= -3:
                boom_sound = pygame.mixer.Sound('boom.wav')
                boom_sound.play()
                scoreboard.you_lose()
                bomb_instance1.kill()
                bomb_instance2.kill()
                bomb_instance3.kill()
                bomb_instance4.kill()
                bomb_instance5.kill()
                bomb_instance6.kill()
                wire_sprites.draw(screen)
                cutters1.bomb_boom()










            # Get the keys that are currently pressed and the mouse pos.
            keys = pygame.key.get_pressed()
            mouse_buttons = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            # gives you a power up if you click the power up.
            if mouse_buttons[0] and clock_power_up_instance.rect.collidepoint(mouse_pos):
                clock_power_up_instance.kill()
                timer_sprite.seconds += 100
                cutters1.strong()

####################################################################################################################################################################################################








        # Constantly updates timer sprite
        timer_sprite.update_timer()

        # Updates the cutters x,y pos on the screen
        cutters1.update(keys)

        # Updates the cut function
        cutters1.cut(keys)

        # Updates the bomb sprites on the screen
        bomb_sprite.update()

        # Fill the screen with a white color
        screen.blit(background, (0,0))

        # Draw cutter sprite
        cutter_sprite.draw(screen)

        # Draw bomb sprites
        bomb_sprite.draw(screen)

        # Draw wire sprites
        wire_sprites.draw(screen)

        # Draw clock power up sprite.
        clock_power_up_group.draw(screen)

        # Update the clock power up sprite
        clock_power_up_group.update()

        # Draw score sprite.
        score_sprite.draw(screen)

        # Update score
        score_sprite.update()


        # Update the display
        pygame.display.flip()


        # Set the frame rate
        clock.tick(fr)


if __name__ == "__main__":
    start_screen()
    main()

