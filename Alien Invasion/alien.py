import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen, type):
        """Initialize the alien and set its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.current = 0
        self.alien_type = type

        # Load the alien image and set its rect attr
        if self.alien_type == 2:
            self.image1 = pygame.image.load('images/alien_1.png')
            self.image2 = pygame.image.load('images/alien_2.png')
        elif self.alien_type == 1:
            self.image1 = pygame.image.load('images/alien_3.png')
            self.image2 = pygame.image.load('images/alien_4.png')
        elif self.alien_type == 0:
            self.image1 = pygame.image.load('images/alien_5.png')
            self.image2 = pygame.image.load('images/alien_6.png')

        self.images = [self.image1, self.image2]
        self.image = self.images[self.current]
        self.rect = self.image1.get_rect()

        # Start each new alien near the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store teh alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image1, self.rect)

    def check_edges(self):
        """Return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        if pygame.time.get_ticks() % 50 == 0:
            self.current = (self.current + 1) % 2
            self.image = self.images[self.current]
