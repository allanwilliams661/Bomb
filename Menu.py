import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 30
COLOR = (100, 100, 100)
BLACK = (0, 0, 0)

# Create the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Diffuse the Bomb')

# Fonts
font = pygame.font.Font('NovaSquare-Regular.ttf', 36)
font2 = pygame.font.Font('NovaSquare-Regular.ttf', 20)


def start_screen():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False  # Exit the start screen when spacebar is pressed

        screen.fill(COLOR)

        # Display text on the start screen
        text = font.render("Press SPACE to start", True, (153, 122, 0))

        # Split instructions into lines
        instructions_line1 = "Diffuse the bomb before the time runs out."
        instructions_line2 = "Cut the wires but be careful."
        instructions_line3 = "If a bomblet touches you while cutting, you'll lose points."
        instructions_line4 = "You can get a speed boost by clicking on the elusive timer bomb."
        instructions_line5 = "Good luck and remember, a steady hand and an expeditious attitude may save your life."

        # Render each line separately
        instruction_1 = font2.render(instructions_line1, True, BLACK)
        instruction_2 = font2.render(instructions_line2, True, BLACK)
        instruction_3 = font2.render(instructions_line3, True, BLACK)
        instruction_4 = font2.render(instructions_line4, True, BLACK)
        instruction_5 = font2.render(instructions_line5, True, BLACK)

        # Position each line of text at the top of the screen with vertical spacing
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        instruction_1_rect = instruction_1.get_rect(top=0, center=(SCREEN_WIDTH // 2, 50)).move(-50, 0)
        instruction_2_rect = instruction_1_rect.move(0, instruction_1.get_height() + 5)
        instruction_3_rect = instruction_2_rect.move(0, instruction_2.get_height() + 5)
        instruction_4_rect = instruction_3_rect.move(0, instruction_3.get_height() + 5)
        instruction_5_rect = instruction_4_rect.move(0, instruction_4.get_height() + 5)

        screen.blit(text, text_rect)
        screen.blit(instruction_1, instruction_1_rect)
        screen.blit(instruction_2, instruction_2_rect)
        screen.blit(instruction_3, instruction_3_rect)
        screen.blit(instruction_4, instruction_4_rect)
        screen.blit(instruction_5, instruction_5_rect)

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)


start_screen()


