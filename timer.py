import pygame
import pygame
import sys

class Timer(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)  # Font for timer text
        self.seconds = 60 * 30  # Initial time in seconds (30 minutes)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        #self.alarm_sound = pygame.mixer.Sound('alarm_sound.wav')  # Load sound file
        self.update_text()

    def update_text(self):
        timer_text = self.font.render(str(self.seconds), True, (0, 0, 0))  # Render the timer text
        text_rect = timer_text.get_rect(center=(self.width / 2, self.height / 2))
        self.image.fill((255, 255, 255))  # Fill the timer background with white
        self.image.blit(timer_text, text_rect)

    def update_timer(self):
        self.seconds -= 1
        if self.seconds <= 0:
            self.seconds = 0
            # Play the alarm sound when the timer reaches zero
            #self.alarm_sound.play()
        if self.seconds < 1000:
            self.font = pygame.font.Font(None, 36)  # Change font to size 36
            self.image.fill((255, 255, 255))  # Fill the timer background with white
            timer_text = self.font.render(str(self.seconds), True, (255, 0, 0))  # Red color for font
            text_rect = timer_text.get_rect(center=(self.width / 2, self.height / 2))
            self.image.blit(timer_text, text_rect)
        else:
            self.update_text()