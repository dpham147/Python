import pygame
import sys


class EventLoop:
    def __init__(self, finished):
        self.finished = finished

    @staticmethod
    def check_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    '''def check_events(screen, pacman, ghosts):
        if event.key in EventLoop.map.keys():
            EventLoop.pacman_moving ='''