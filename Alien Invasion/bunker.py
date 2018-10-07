import pygame
from pygame.sprite import Sprite
from PIL import Image
import random


class Bunker(Sprite):
    def __init__(self, screen, ship):
        super(Bunker, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Load bunker image
        self.pixel_image = Image.open('images/bunker.png')

        self.redraw()

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()

        # Spawn at top left
        self.rect.x = self.rect.width
        self.rect.bottom = self.screen_rect.bottom - ship.rect.height * 1.5

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def eat(self):
        for i in range(self.pixel_image.size[0]):
            for j in range(self.pixel_image.size[1]):
                rndm = random.randint(0, 4)
                if rndm == 0:
                    self.pixels[i, j] = (0, 0, 0, 0)
        self.redraw()

    def redraw(self):
        mode = self.pixel_image.mode
        size = self.pixel_image.size
        data = self.pixel_image.tobytes()

        self.pixels = self.pixel_image.load()

        self.image = pygame.image.fromstring(data, size, mode)
