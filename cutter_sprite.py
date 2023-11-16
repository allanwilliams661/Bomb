import pygame


class Cutter(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, cutter_width: int, cutter_height: int, image_path=None) -> None:
        super().__init__()
        self.rect = pygame.Rect(x, y, cutter_width, cutter_height)
        self.speed = 5
        self.sound = pygame.mixer.Sound('snip.wav')
        self.sound_playing = False
        if image_path:
            # Defines the image path
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (cutter_width, cutter_height))


        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, keys: pygame.key.get_pressed) -> None:
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:  # Adjust 800 based on your screen width
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < 600:  # Adjust 600 based on your screen height
            self.rect.y += self.speed
        if keys[
            pygame.K_SPACE] and not self.sound_playing:  # Check if space bar is pressed and sound is not already playing
            self.sound.play()  # Play the sound when space bar is pressed
            self.sound_playing = True  # Set flag to True when sound is playing
        elif not keys[pygame.K_SPACE]:
            self.sound_playing = False














