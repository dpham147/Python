import pygame
from pygame.sprite import Sprite


class Alien_Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, alien):
        """Create a bullet object at the ship's current position"""
        super(Alien_Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set the correct position.
        self.image = pygame.image.load('images/alien_bullet.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.speed_factor = ai_settings.alien_bullet_speed_factor

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y += self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def blitme(self):
        """Draw the bullet to screen"""
        self.screen.blit(self.image, self.rect)
