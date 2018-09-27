import random
import pygame


class Settings():
    """Class to store all settings for pong"""

    def __init__(self):
        """Inits the game's settings"""
        # Screen
        display = pygame.display.Info()
        self.screen_width = 1200
        self.screen_height = 500
        self.bg_color = (0, 0, 0)

        # Font sizes
        self.title_font = 48
        self.text_font_size = 36

        # Ball settings
        self.ball_color = (255, 255, 255)
        self.ball_radius = 10
        self.ball_diameter = self.ball_radius * 2
        self.ball_speedup = 1.1
        self.adj_threshold = 0.05
        self.adj_factor = 0.05
        self.min_velocity = .8
        self.max_velocity = 1
        self.abs_max_vel = 1.25

        # Paddle settings
        self.paddle_x = 5
        self.paddle_y = 120
        self.paddle_width = 10
        self.paddle_height = 200
        self.paddle_color = (255, 255, 255)
        self.paddle_speed = .5

        # Divider settings
        self.divider_color = (255, 255, 255)
        self.divider_width = 1
        self.divider_height = self.screen_height

        # Scoring settings
        self.score_target = 5

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        ran_dir_x = random.uniform(-1, 1)
        ran_dir_y = random.uniform(-1, 1)
        magnitude_x = random.uniform(self.min_velocity, self.max_velocity)
        magnitude_y = random.uniform(self.min_velocity, self.max_velocity)
        self.x_velocity, self.y_velocity = ran_dir_x * magnitude_x, ran_dir_y * magnitude_y
