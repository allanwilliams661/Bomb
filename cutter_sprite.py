import pygame


class Cutter(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, cutter_width: int, cutter_height: int, image_path=None) -> None:
        super().__init__()
        self.rect = pygame.Rect(x, y, cutter_width, cutter_height)
        self.speed = 5
        self.sound = pygame.mixer.Sound('snip.wav')
        self.sound_playing = False

            # Defines the image of the sprite
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (cutter_width, cutter_height))

        # Get/Define the rect and pos of cutter sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    # Make a method that makes the cutter sprite move
    def update(self, keys: pygame.key.get_pressed) -> None:
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:  # Make it so it cant go off screen
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < 600:  # Make it so it cant go off screen
            self.rect.y += self.speed



    def cut(self, keys: pygame.key.get_pressed) -> None:
        if keys[
            pygame.K_SPACE] and not self.sound_playing:  # Check if space bar is pressed and sound is not already playing
            self.sound.play()  # Play the sound when space bar is pressed
            self.sound_playing = True  # Set flag to True when sound is playing
        elif not keys[pygame.K_SPACE]:
            self.sound_playing = False

    def weak(self):
        self.speed = 2
        self.image_path = 'nail_clip.png'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))
    def strong(self):
        self.speed = 6
        self.image_path = 'wire_cut.png'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))
    def bomb_boom(self):

        self.image_path = 'boom_image.png'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (300, 300))

















