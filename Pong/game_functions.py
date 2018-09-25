import sys
from time import sleep
import pygame
from paddle import Paddle
from ball import Ball
from cpu_agent import Computer


def check_keydown_events(event, paddle, stats):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        paddle.moving_down = True
    elif event.key == pygame.K_w or event.key == pygame.K_UP:
        paddle.moving_up = True
    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        paddle.moving_left = True
    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        paddle.moving_right = True
    elif event.key == pygame.K_SPACE:
        stats.game_active = True


def check_keyup_events(event, paddle):
    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
        paddle.moving_down = False
    elif event.key == pygame.K_w or event.key == pygame.K_UP:
        paddle.moving_up = False
    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        paddle.moving_left = False
    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        paddle.moving_right = False


def check_events(settings, screen, ball, paddle, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddle, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle)


def check_collision(settings, ball, paddle):
    circle = ball.circle
    # Check collision with left and right paddles
    if circle.colliderect(paddle.rect1) or circle.colliderect(paddle.rect2) or \
            circle.colliderect(paddle.cpu1) or circle.colliderect(paddle.cpu2):
            ball.x_velocity *= settings.ball_speedup
            ball.y_velocity *= -settings.ball_speedup
    # Check if collides with bottom paddle
    if ball.circle.colliderect(paddle.rect3) or circle.colliderect(paddle.cpu3):
        ball.y_velocity *= settings.ball_speedup
        ball.x_velocity *= -settings.ball_speedup

    adjust_speed(settings, ball)


def adjust_speed(settings, ball): #TODO: Allow autoadjustment of ball speed should it come close to cardinal
    eggs = 0


def check_out_of_bounds(settings, screen, ball, game_stats, scoreboard):
    screen_rect = screen.get_rect()
    if ball.circle.left <= 0 or \
            ball.circle.top <= 0 or \
            ball.circle.right >= screen_rect.right or \
            ball.circle.bottom >= screen_rect.bottom:
        ball.reset()
        settings.init_dynamic_settings()

        if ball.circle.centerx < screen_rect.centerx:
            game_stats.cpu_score += 1
        elif ball.circle.centerx >= screen_rect.centerx:
            game_stats.player_score += 1
        scoreboard.prep_scores()

        sleep(0.5)


def display_start_screen(settings, screen):

    screen_rect = screen.get_rect()

    # Recolor screen
    screen.fill(settings.bg_color)
    title_str = "PONG"
    text_color = (255, 255, 255)
    font = pygame.font.SysFont(None, 48)

    title_image = font.render(title_str, True, text_color, settings.bg_color)

    title_image_rect = title_image.get_rect()
    title_image_rect.centerx = screen_rect.centerx
    title_image_rect.centery = screen_rect.centery - 40

    pygame.display.flip()


def update_screen(settings, screen, ball, paddle, scoreboard, game_stats):
    # Recolor the screen
    screen.fill(settings.bg_color)

    # Check for collisions
    check_collision(settings, ball, paddle)

    # Check for boundaries
    check_out_of_bounds(settings, screen, ball, game_stats, scoreboard)

    # Redraw the ball
    ball.draw_ball()

    # Redraw the paddle
    paddle.draw_paddle()

    # Redraw scores
    scoreboard.show_scores()

    pygame.display.flip()
