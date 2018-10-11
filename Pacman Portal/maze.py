import pygame
from imagerect import ImageRect


class Maze():

    red = (255, 0, 0)
    BRICK_SIZE = 13

    def __init__(self, screen, mazefile, brickfile, portalfile, shieldfile, pointfile):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.bricks = []
        self.shields = []
        self.hori_portals = []
        self.vert_portals = []
        self.points = []
        sz = Maze.BRICK_SIZE
        self.brick = ImageRect(screen, brickfile, sz, sz)
        self.shield = ImageRect(screen, shieldfile, sz, sz)
        self.hori_portal = ImageRect(screen, portalfile, sz, 5 * sz)
        self.vert_portal = ImageRect(screen, portalfile, 5 * sz, sz)
        self.vert_portal.image = pygame.transform.rotate(self.hori_portal.image, 90)
        self.point = ImageRect(screen, pointfile, int(.5 * sz), int(.5 * sz))

        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.build()

    def build(self):
        rect = self.brick.rect
        w, h = rect.width, rect.height
        dx, dy = self.deltax, self.deltay

        rshield = self.shield.rect
        rvportal = self.vert_portal.rect
        rhportal = self.hori_portal.rect
        rpoint = self.point.rect

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'X':
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'o':
                    self.shields.append(pygame.Rect(ncol * dx, nrow * dy, rshield.width, rshield.height))
                elif col == 'h':
                    self.hori_portals.append(pygame.Rect(ncol * dx, nrow * dy, rhportal.width, rhportal.height))
                elif col == 'v':
                    self.vert_portals.append(pygame.Rect(ncol * dx, nrow * dy, rvportal.width, rvportal.height))
                elif col == 'p':
                    self.points.append(pygame.Rect(ncol * dx, nrow * dy, rpoint.width, rpoint.height))

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
        for rect in self.shields:
            self.screen.blit(self.shield.image, rect)
        for rect in self.hori_portals:
            self.screen.blit(self.hori_portal.image, rect)
        for rect in self.vert_portals:
            self.screen.blit(self.vert_portal.image, rect)
        for rect in self.points:
            self.screen.blit(self.point.image, rect)
