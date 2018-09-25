import pygame
from paddle import Paddle


class Computer:

    def __init__(self, settings, screen, ball):
        self.paddles = Paddle(settings, screen)
        self.ball = ball

    def update(self, ball, paddles):
        if ball.x < paddles.cpu1.centerx:
            paddles.cpu_moving_left = True
            paddles.cpu_moving_right = False
        elif ball.x >= paddles.cpu1.centerx:
            paddles.cpu_moving_right = True
            paddles.cpu_moving_left = False

        if ball.y < paddles.cpu3.centery:
            paddles.cpu_moving_up = True
            paddles.cpu_moving_down = False
        elif ball.y >= paddles.cpu3.centery:
            paddles.cpu_moving_up = False
            paddles.cpu_moving_down = True
