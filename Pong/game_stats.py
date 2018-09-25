class GameStats():
    """Tracks the game stats"""

    def __init__(self, settings):
        self.settings = settings
        self.target_score = settings.score_target

        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.player_score = 0
        self.cpu_score = 0