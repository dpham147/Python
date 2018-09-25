import pygame
from pygame.sprite import Group
from paddle import Paddle
from ball import Ball
from game_settings import Settings
import game_functions as gf


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Pong")

    # Make player
    paddle = Paddle(settings, screen)
    paddle.top = 100
    paddle.left = 50

    # Create the ball
    ball = Ball(settings, screen)

    while True:
        gf.check_events(settings, screen, ball, paddle)

        paddle.update()
        ball.update()
        gf.update_screen(settings, screen, ball, paddle)


run_game()