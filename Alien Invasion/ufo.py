import pygame
from pygame.sprite import Sprite


class UFO(Sprite):

    def __init__(self, ai_settings, screen):
        super(UFO, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.alien_type = 3
        self.image = pygame.image.load('images/ufo.png')

        self.rect = self.image.get_rect()
        self.rect.right = self.screen_rect.left
        self.rect.y = self.screen_rect.top + 50

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        if self.rect.right < 0:
            self.ai_settings.ufo_direction = 1
            self.ai_settings.ufo_move = False
        elif self.rect.left > self.screen_rect.right:
            self.ai_settings.ufo_direction = -1
            self.ai_settings.ufo_move = False

    def update(self):
        if self.ai_settings.ufo_move:
            self.x += (self.ai_settings.ufo_speed_factor * self.ai_settings.ufo_direction)
            self.rect.x = self.x
            self.check_edges()
