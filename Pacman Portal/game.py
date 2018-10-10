import pygame
from maze import Maze
from eventloop import EventLoop

class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((680, 740))
        pygame.display.set_caption("Pacman Portal")

        self.maze = Maze(self.screen, mazefile='images/packmanportalmaze.txt',
                         brickfile='square', portalfile='portal',
                         shieldfile='shield', pointfile='point')

    def play(self):
        eloop = EventLoop(finished=False)
        while not eloop.finished:
            eloop.check_events()
            self.update_screen()

   def update_screen(self):
       self.screen.fill(self.BLACK)