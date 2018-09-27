import pygame.font

class Scoreboard():
    """Scoring Interface"""

    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats
        
        # Font settings
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, self.settings.text_font_size)
        
        # Prep initial score images
        self.prep_scores()

    def prep_scores(self):
        player_score = self.stats.player_score
        player_score_str = "{:,}".format(player_score)
        player_score_str = "Your Score: " + player_score_str
        self.player_score_image = self.font.render(player_score_str, True, self.text_color, self.settings.bg_color)

        self.player_score_rect = self.player_score_image.get_rect()
        self.player_score_rect.left = self.screen_rect.left + 20
        self.player_score_rect.top = 20

        cpu_score = self.stats.cpu_score
        cpu_score_str = "{:,}".format(cpu_score)
        cpu_score_str = "CPU Score: " + cpu_score_str
        self.cpu_score_image = self.font.render(cpu_score_str, True, self.text_color, self.settings.bg_color)

        self.cpu_score_rect = self.cpu_score_image.get_rect()
        self.cpu_score_rect.right = self.screen_rect.right - 20
        self.cpu_score_rect.top = 20

    def show_scores(self):
        """Draw score to screen"""
        self.screen.blit(self.player_score_image, self.player_score_rect)
        self.screen.blit(self.cpu_score_image, self.cpu_score_rect)
