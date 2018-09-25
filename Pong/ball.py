import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """A class to manage the ball object"""

    def __init__(self, settings, screen):
        """Creates a ball at location in settings"""
        super(Ball, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        # Creates "ball" at given location
        self.circle = pygame.Rect(0, 0, settings.ball_diameter, settings.ball_diameter)
        self.circle.center = self.screen_rect.center
        self.pos = self.circle.center

        # Store ball's pos as decimal value
        self.x = float(self.circle.x)
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
        self.pos = self.circle.center

    def draw_ball(self):
        #pygame.draw.Rect(self.screen, self.color, self.circle)
        pygame.draw.circle(self.screen, self.color, self.pos, self.settings.ball_radius)

    def reset(self):
        self.x = self.screen_rect.centerx
        self.y = self.screen_rect.centery
        self.x_velocity = self.settings.x_velocity
        self.y_velocity = self.settings.y_velocity
