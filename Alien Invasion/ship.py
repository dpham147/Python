import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set it's starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load animations
        self.sheet = pygame.image.load('images/ship_sheet.png')
        self.frames = self.load_sprites(self.sheet)
        self.frame = 0

        # Load the ship image and get its rect.
        self.image = self.frames[self.frame]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        self.mask = pygame.mask.from_surface(self.image)

    def load_sprites(self, sheet):
        frames = []
        for i in range(11):
            location = (0, (32 * i) + 1)
            frames.append(sheet.subsurface(pygame.Rect(location, (50, 20))))
        return frames

    def update(self):
        """Update teh ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def destroy(self):
        if self.frame == 11:
            self.frame = 0
            self.image = self.frames[self.frame]
            self.blitme()
        elif pygame.time.get_ticks() % 1000 == 0:
            self.frame += 1
            self.image = self.frames[self.frame]
            self.blitme()
            self.destroy()

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center ship on screen"""
        self.center = self.screen_rect.centerx
        self.image = self.frames[self.frame]