import pygame
from maze import Maze
from eventloop import EventLoop


class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((680, 740))
        pygame.display.set_caption("Pacman Portal")

        self.maze = Maze(self.screen, mazefile='images/pacmanportalmaze.txt',
                         brickfile='map_block', portalfile='portal',
                         shieldfile='shield', pointfile='point')

    def play(self):
        eloop = EventLoop(finished=False)
        while not eloop.finished:
            eloop.check_events()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        self.maze.blitme()
        pygame.display.flip()


game = Game()
game.play()
