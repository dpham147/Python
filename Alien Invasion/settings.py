class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.menu_bg_color = (0, 0, 0)
        self.game_bg_color = (0, 0, 255)
        self.font_color = (255, 255, 255)
        self.title_font_size = 100
        self.sub_title_font_size = 80
        self.menu_font_size = 48

        # View mode
        self.show_menu = True
        self.show_high_scores = False
        self.show_game = False

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10
        self.alien_bullet_speed_factor = 1

        # UFO settings
        self.ufo_direction = 1
        self.ufo_speed_factor = 4
        self.ufo_move = False
        self.ufo_show_score = False
        self.ufo_score_center = 0
        self.ufo_score_delay = 500

        # Game speedup scale
        self.speedup_scale = 1.1

        # Score bonus scale
        self.score_scale = 1.0

        # Audio settings
        self.laser_sound = 'audio/laser.wav'
        self.bgm = 'audio/bgm.wav'
        self.game_over = 'audio/gameover.wav'

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1
        self.alien_fire_rate = 10000

        # Fleet direction of 1 represents right; -1 for left
        self.fleet_direction = 1

        # Scoring
        self.alien_points_1 = 50
        self.alien_points_2 = 75
        self.alien_points_3 = 100
        self.ufo_points = 1000

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_fire_rate /= self.speedup_scale * 2

        self.alien_points_1 = int(self.alien_points_1 * self.score_scale)
        self.alien_points_2 = int(self.alien_points_2 * self.score_scale)
        self.alien_points_3 = int(self.alien_points_3 * self.score_scale)
        self.ufo_points = int(self.ufo_points * self.score_scale)