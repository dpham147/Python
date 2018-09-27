import pygame
from paddle import Paddle
from ball import Ball
from game_settings import Settings
from cpu_agent import Computer
from game_stats import GameStats
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Pong")

    # Make paddles
    paddle = Paddle(settings, screen)

    # Create the ball
    ball = Ball(settings, screen)

    # Setup the computer player
    cpu = Computer(settings, screen, ball)

    # Create scoring board
    stats = GameStats(settings)
    scoreboard = Scoreboard(settings, screen, stats)

    while True:
        gf.check_events(settings, screen, ball, paddle, stats)

        if stats.game_active:
            paddle.update()
            ball.update()
            cpu.update(ball, paddle)
            gf.update_screen(settings, screen, ball, paddle, scoreboard, stats)
        else:
            gf.display_start_screen(settings, screen)


run_game()
