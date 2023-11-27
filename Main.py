from cutter_sprite import *
from wires import *
from timer import *


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
    # Create cutter instance with image
    cutters = Cutter(50, 50, 50, 50, image_path="wire_cut.png")
    timer_sprite = Timer(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 200, 100)

    # Make wire sprite instances
    wire_instance1 = Wires(100, 100, 200, 10)
    wire_instance2 = Wires(100, 400, 200, 10)
    wire_instance3 = Wires(400, 400, 200, 10)
    wire_instance4 = Wires(400, 100, 200, 10)
    cutter_sprite.add(cutters)
    wire_sprites.add(wire_instance1, wire_instance2, wire_instance3, wire_instance4)
    wire_sprites.add(timer_sprite)
    wire_list = list(wire_sprites.sprites())

    correct_wire = random.randint(1, 4)

    if correct_wire == 1:
        wire_color = 'red'
    elif correct_wire == 2:
        wire_color = 'blue'
    elif correct_wire == 3:
        wire_color = 'green_yellow'
    elif correct_wire == 4:
        wire_color = 'pink'

    score = 0

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
                    wire.kill()



        # Get the keys that are currently pressed. Could be redundant**
        keys = pygame.key.get_pressed()
        # Move the cutter based on the arrow keys
        cutters.update(keys)
        cutters.cut(keys)
        # Fill the screen with a white color
        screen.fill((255, 255, 255))
        # Draw cutter sprite
        cutter_sprite.draw(screen)
        # Draw wire sprites
        wire_sprites.draw(screen)

        timer_sprite.update_timer()
        # Update the display
        pygame.display.flip()


        # Set the frame rate
        clock.tick(30)


if __name__ == "__main__":
    main()
