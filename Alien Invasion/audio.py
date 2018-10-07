import pygame


class Audio():
    def __init__(self, ai_settings):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(3)

        pygame.mixer.music.load(ai_settings.bgm)
        pygame.mixer.music.play(-1)

        self.laser = pygame.mixer.Sound(ai_settings.laser_sound)
        self.gameover = pygame.mixer.Sound(ai_settings.game_over)

    def play_laser(self):
        pygame.mixer.Channel(1).play(self.laser)
        pygame.mixer.Channel(1).set_volume(.1)

    def play_gameover(self):
        pygame.mixer.Channel(2).play(self.gameover)
        pygame.mixer.Channel(2).set_volume(.1)
