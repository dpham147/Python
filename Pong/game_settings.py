import random


class Settings():
    """Class to store all settings for pong"""

    def __init__(self):
        """Inits the game's settings"""
        # Screen
        self.screen_width = 400
        self.screen_height = 400
        self.bg_color = (0, 0, 0)

        # Ball settings
        self.ball_pos_x = self.screen_width / 2
        self.ball_pos_y = self.screen_height / 2
        self.x_velocity = .1
        self.y_velocity = 0
        self.ball_color = (255, 255, 255)
        self.ball_diameter = 10

        # Paddle settings
        self.paddle_x = 5
        self.paddle_y = 120
        self.paddle_width = 20
        self.paddle_height = 200
        self.paddle_color = (255, 255, 255)
        self.paddle_speed = .5

