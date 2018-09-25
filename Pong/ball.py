import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """A class to manage the ball object"""

    def __init__(self, settings, screen):
        """Creates a ball at location in settings"""
        super(Ball, self).__init__()
        self.screen = screen
        screen_rect = screen.get_rect()

        # Creates "ball" at given location
        self.circle = pygame.Rect(0, 0, settings.ball_diameter, settings.ball_diameter)
        self.circle.center = screen_rect.center

        # Store ball's pos as decimal value
        self.x = float(self.circle.y)
        self.y = float(self.circle.y)
        self.x_velocity = settings.x_velocity
        self.y_velocity = settings.y_velocity

        self.color = settings.ball_color

    def update(self):
        # Update decimal pos of ball
        self.x += self.x_velocity
        self.y += self.y_velocity

        self.circle.x = self.x
        self.circle.y = self.y

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.color, self.circle)
