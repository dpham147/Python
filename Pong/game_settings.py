import random
import math


class Settings():
    """Class to store all settings for pong"""

    def __init__(self):
        """Inits the game's settings"""
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ball settings
        self.ball_color = (255, 255, 255)
        self.ball_radius = 5
        self.ball_diameter = 10
        self.ball_speedup = 1.1
        self.adj_threshold = 0.05
        self.adj_factor = 0.05

        # Paddle settings
        self.paddle_x = 5
        self.paddle_y = 120
        self.paddle_width = 10
        self.paddle_height = 200
        self.paddle_color = (255, 255, 255)
        self.paddle_speed = .5

        # Scoring settings
        self.score_target = 5

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        self.x_velocity, self.y_velocity = random.uniform(-1, 1), random.uniform(-1, 1)
