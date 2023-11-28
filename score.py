import pygame


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, x, y, font=None):
        super().__init__()
        self.score = 0
        self.font = font
        self.image = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update_score(self):
        self.image = self.font.render(f"Score: {self.score}", True, (0, 0, 0))

    def increase_score(self):
        self.score += 1

    def decrease_score(self):
        self.score -= 1
