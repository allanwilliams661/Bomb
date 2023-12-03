import pygame
import pygame
import sys

class Timer(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x # X pos
        self.y = y # Y pos
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)  # Font for timer text
        self.seconds = 60 * 30  # Initial time 30 seconds. Based on clock fps speed
        self.image = pygame.Surface((width, height)) # Makes a blank surface on which to blit
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.update_text()

    def update_text(self):
        timer_text = self.font.render(str(self.seconds), True, (0, 0, 0))  # Render the timer text from the time
        text_rect = timer_text.get_rect(center=(self.width / 2, self.height / 2))
        self.image.fill((255, 255, 255))  # Fill the timer background with white
        self.image.blit(timer_text, text_rect) # Continously blits the text to the screen

    # Update the time left
    def update_timer(self):
        self.seconds -= 1
        if self.seconds <= 0:
            self.seconds = 0
        # Make it so it changes color to let the player know they are running out of time.
        if self.seconds < 1000:
            self.font = pygame.font.Font(None, 36)  # Set font
            self.image.fill((70, 100, 45))  # Fill the timer background with green
            timer_text = self.font.render(str(self.seconds), True, (255, 0, 0))  # Red color for font
            text_rect = timer_text.get_rect(center=(self.width / 2, self.height / 2))
            self.image.blit(timer_text, text_rect)
        else:
            self.update_text()

    def power_up(self):
        self.seconds += 300
