
from cutter_sprite import *


def main() -> None:
    # Initialize Pygame
    pygame.init()

    # Set up display
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Move Cutter with Arrow Keys")

    # Create a sprite group
    all_sprites: Group = pygame.sprite.Group()

    # Create a cutter instance with an image (provide the path to your image)
    cutters = Cutter(50, 50, 50, 50, image_path="wire_cut.png")
    all_sprites.add(cutters)

    # Main game loop
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get the keys that are currently pressed
        keys = pygame.key.get_pressed()

        # Move the cutter based on the keys
        cutters.move(keys)

        # Fill the screen with a white color
        screen.fill((255, 255, 255))

        # Draw all sprites in the group
        all_sprites.draw(screen)

        # Update the display
        pygame.display.flip()

        # Set the frame rate
        clock.tick(30)

if __name__ == "__main__":
    main()





