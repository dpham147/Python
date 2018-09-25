import sys
import pygame
from paddle import Paddle
from ball import Ball


def check_keydown_events(event, paddle):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        paddle.moving_down = True
    elif event.key == pygame.K_w or event.key == pygame.K_UP:
        paddle.moving_up = True


def check_keyup_events(event, paddle):
    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
        paddle.moving_down = False
    if event.key == pygame.K_w or event.key == pygame.K_UP:
        paddle.moving_up = False


def check_events(settings, screen, ball, paddle):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddle)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle)


def check_collision(settings, screen, ball, paddle):
    if ball.circle.bottom > paddle.rect1.top and ball.circle.top < paddle.rect1.bottom:
        if ball.circle.right >= paddle.rect2.left or ball.circle.left <= paddle.rect1.right:
            ball.x_velocity *= -1
    # elif ball.circle.centerx >= paddle.rect2.left and ball.circle.centerx <= paddle.rect2.right:
    check_out_of_bounds(settings, screen, ball)


def check_out_of_bounds(settings, screen, ball):
    screen_rect = screen.get_rect()
    if ball.circle.left <= 0 or \
            ball.circle.top <= 0 or \
            ball.circle.right >= screen_rect.right or \
            ball.circle.bottom >= screen_rect.bottom:
        c = 0


def update_screen(settings, screen, ball, paddle):
    # Recolor the screen
    screen.fill(settings.bg_color)

    # Check for collisions
    check_collision(settings, screen, ball, paddle)

    # Redraw the ball
    ball.draw_ball()

    # Redraw the paddle
    paddle.draw_paddle()

    pygame.display.flip()
