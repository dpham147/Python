import pygame
from pygame.sprite import Sprite


class Paddle():

    def __init__(self, settings, screen):
        super(Paddle, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.color = settings.paddle_color

        """Create Left Paddle"""
        self.rect1 = pygame.Rect(0, 0, settings.paddle_width,
                                 settings.paddle_height)

        """Create Right Paddle"""
        self.rect2 = pygame.Rect(0, 0, settings.paddle_width,
                                 settings.paddle_height)

        # Correct paddle positions
        self.rect1.top, self.rect2.top = 100, 100
        self.rect1.left = 50
        self.rect2.right = self.screen_rect.right - 50

        # Holds y value for both paddles
        self.y = float(self.rect1.y)

        # Movement booleans
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_down and self.rect1.bottom < self.screen_rect.bottom:
            self.y += self.settings.paddle_speed
        if self.moving_up and self.rect1.top > 0:
            self.y -= self.settings.paddle_speed

        self.rect1.y = self.y
        self.rect2.y = self.y

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, self.rect1)
        pygame.draw.rect(self.screen, self.color, self.rect2)