from game_functions import get_highscores

class GameStats():
    """Track stats for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start game in an inactive state
        self.game_active = False
        # High score (should never be reset)
        highscores = get_highscores()
        self.high_score = int(highscores[0])

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.player_score = 0
        self.level = 1

