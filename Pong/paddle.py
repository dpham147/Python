import pygame


class Paddle():

    def __init__(self, settings, screen):
        super(Paddle, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.screen_half = self.screen_rect.width / 2
        self.settings = settings
        self.color = settings.paddle_color

        """Create Top Paddle"""
        self.rect1 = pygame.Rect(0, 0, settings.paddle_height,
                                 settings.paddle_width)

        """Create Bottom Paddle"""
        self.rect2 = pygame.Rect(0, 0, settings.paddle_height,
                                 settings.paddle_width)

        """Create Left Paddle"""
        self.rect3 = pygame.Rect(0, 0, settings.paddle_width,
                                 settings.paddle_height)

        """Create CPU Top Paddle"""
        self.cpu1 = pygame.Rect(0, 0, settings.paddle_height,
                                settings.paddle_width)

        """Create CPU Bottom Paddle"""
        self.cpu2 = pygame.Rect(0, 0, settings.paddle_height,
                                settings.paddle_width)

        """Create CPU Left Paddle"""
        self.cpu3 = pygame.Rect(0, 0, settings.paddle_width,
                                settings.paddle_height)

        self.reset()

    def update(self):
        if self.moving_down and self.rect3.bottom < self.screen_rect.bottom:
            self.y += self.settings.paddle_speed
        if self.moving_up and self.rect3.top > 0:
            self.y -= self.settings.paddle_speed

        if self.moving_left and self.rect1.left > self.screen_rect.left:
            self.x -= self.settings.paddle_speed
        if self.moving_right and self.rect1.right < self.screen_rect.centerx:
            self.x += self.settings.paddle_speed

        if self.cpu_moving_down and self.cpu3.bottom < self.screen_rect.bottom:
            self.cpu_y += self.settings.paddle_speed
        if self.cpu_moving_up and self.cpu3.top > 0:
            self.cpu_y -= self.settings.paddle_speed

        if self.cpu_moving_left and self.cpu1.left > self.screen_rect.right / 2:
            self.cpu_x -= self.settings.paddle_speed
        if self.cpu_moving_right and self.cpu1.right < self.screen_rect.right:
            self.cpu_x += self.settings.paddle_speed

        self.rect1.x = self.x
        self.rect2.x = self.x
        self.rect3.y = self.y
        self.cpu1.x = self.cpu_x
        self.cpu2.x = self.cpu_x
        self.cpu3.y = self.cpu_y

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, self.rect1)
        pygame.draw.rect(self.screen, self.color, self.rect2)
        pygame.draw.rect(self.screen, self.color, self.rect3)
        pygame.draw.rect(self.screen, self.color, self.cpu1)
        pygame.draw.rect(self.screen, self.color, self.cpu2)
        pygame.draw.rect(self.screen, self.color, self.cpu3)

    def reset(self):
        # Correct paddle positions
        self.rect1.top = 0
        self.rect1.centerx = self.screen_rect.centerx / 2
        self.rect2.bottom = self.screen_rect.bottom
        self.rect2.centerx = self.screen_rect.centerx / 2
        self.rect3.centery = self.screen_rect.centery
        self.rect3.left = 0

        self.cpu1.top = 0
        self.cpu1.centerx = self.screen_rect.width * 3 / 4
        self.cpu2.bottom = self.screen_rect.bottom
        self.cpu2.centerx = self.screen_rect.width * 3 / 4
        self.cpu3.centery = self.screen_rect.centery
        self.cpu3.right = self.screen_rect.right

        # Holds y value for both paddles
        self.x = float(self.rect1.x)
        self.y = float(self.rect3.y)

        self.cpu_x = float(self.cpu1.x)
        self.cpu_y = float(self.cpu3.y)

        # Movement booleans
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.cpu_moving_up = False
        self.cpu_moving_down = False
        self.cpu_moving_left = False
        self.cpu_moving_right = False
