import pygame.sprite
from timer import Timer


class Pacman:

    def __init__(self):

    def update(self):
    super.update()
    self.rect.x = self.posn.x
    self.rect.y = self.posn.y
    if (self.moving and not self.playing):
        pygame.mixer

    def blit(self):
        imgrect = self.timer.imagerect() if not self.dead else self.timerdead.imagerect()
        angle = Pacman.rotations[self.direction]
        img = pygame.transform.rotate(imgrect.image, angle)