import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from ufo import UFO
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from audio import Audio
import game_functions as gf


def run_game():
    # Initialize pygame, settings, and create as screen object
    pygame.init()
    pygame.mixer.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the play button
    play_button = Button(ai_settings, screen, "Play")

    # Create audio controller
    audio = Audio(ai_settings)

    # Make a ship, a group of bullets, a group of aliens, and a group of bunkers
    ship = Ship(ai_settings, screen)
    bullets = Group()
    alien_bullets = Group()
    aliens = Group()
    bunkers = Group()
    ufo = Group()

    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create set of bunkers
    gf.setup_bunkers(screen, ship, bunkers)

    # Create an instance to store game stats and scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, bunkers, aliens, bullets, alien_bullets, audio)

        if stats.game_active:
            ship.update()
            ufo.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, bunkers, alien_bullets, ufo, audio)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets, bunkers, alien_bullets, audio)

        if ai_settings.show_game:
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, bunkers, alien_bullets, ufo)
        elif ai_settings.show_menu:
            gf.display_menu(ai_settings, screen)
        elif ai_settings.show_high_scores:
            gf.display_high_scores(ai_settings, screen)


run_game()

