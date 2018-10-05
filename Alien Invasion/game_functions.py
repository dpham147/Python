import sys
from time import sleep
import pygame
import pygame.font
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_s and ai_settings.show_menu:
        ai_settings.show_menu = False
        ai_settings.show_game = True
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)
    elif event.key == pygame.K_h and ai_settings.show_menu:
        ai_settings.show_menu = False
        ai_settings.show_high_scores = True
    elif event.key == pygame.K_q and ai_settings.show_high_scores:
        ai_settings.show_high_scores = False
        ai_settings.show_menu = True
    elif event.key == pygame.K_q and ai_settings.show_game:
        ai_settings.show_game = False
        ai_settings.show_menu = True
    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet"""
    # Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Respond to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #    mouse_x, mouse_y = pygame.mouse.get_pos()
        #    check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Start a new game when player hits play"""
    # Reset game settings
    ai_settings.initialize_dynamic_settings()

    # Hide the mouse cursor
    pygame.mouse.set_visible(False)

    # Reset game stats
    stats.reset_stats()
    stats.game_active = True

    # Reset scoreboard
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()
        
    # Empty list of aliens and bullets
    aliens.empty()
    bullets.empty()
        
    # Create a new fleet and center ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.game_bg_color)

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Draw the score info
    sb.show_score()

    # Draw the play button if the game is inactive
    # if not stats.game_active:
    #    play_button.draw_button()

    # Display game over if game not active and in game)
    if not stats.game_active and ai_settings.show_game:
        display_gameover(screen, ai_settings)

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def display_gameover(screen, ai_settings):
    screen_rect = screen.get_rect()
    font = pygame.font.SysFont(None, ai_settings.menu_font_size)
    gameover = "GAME OVER"
    gameover_img = font.render(gameover, True, (0, 255, 0), ai_settings.game_bg_color)
    gameover_rect = gameover_img.get_rect()
    gameover_rect.centerx = screen_rect.centerx
    gameover_rect.centery = screen_rect.centery
    screen.blit(gameover_img, gameover_rect)

    gameover = "PRESS [Q] TO RETURN TO MENU"
    gameover_img = font.render(gameover, True, (0, 255, 0), ai_settings.game_bg_color)
    gameover_rect = gameover_img.get_rect()
    gameover_rect.centerx = screen_rect.centerx
    gameover_rect.centery = screen_rect.centery + 40
    screen.blit(gameover_img, gameover_rect)


def display_menu(ai_settings, screen):

    screen_rect = screen.get_rect()
    center_screen = screen_rect.centerx

    screen.fill(ai_settings.menu_bg_color)

    title = "SPACE"
    sub_title = "INVADERS"
    play_button = "PRESS [S] TO START"
    high_score = "PRESS [H] TO VIEW HIGH SCORES"

    white_color = (255, 255, 255)
    green_color = (0, 255, 0)
    title_font = pygame.font.SysFont(None, ai_settings.title_font_size)
    sub_title_font = pygame.font.SysFont(None, ai_settings.sub_title_font_size)
    menu_font = pygame.font.SysFont(None, ai_settings.menu_font_size)

    title_image = title_font.render(title, True, white_color, ai_settings.menu_bg_color)
    subtitle_image = sub_title_font.render(sub_title, True, green_color, ai_settings.menu_bg_color)
    play_image = menu_font.render(play_button, True, green_color, ai_settings.menu_bg_color)
    scores_image = menu_font.render(high_score, True, white_color, ai_settings.menu_bg_color)

    title_rect = title_image.get_rect()
    subtitle_rect = subtitle_image.get_rect()
    play_rect = play_image.get_rect()
    scores_rect = scores_image.get_rect()

    title_rect.centerx = center_screen
    title_rect.top = 50
    subtitle_rect.centerx = center_screen
    subtitle_rect.centery = 140
    play_rect.centerx = center_screen
    play_rect.centery = screen_rect.bottom - 120
    scores_rect.centerx = center_screen
    scores_rect.centery = screen_rect.bottom - 40

    screen.blit(title_image, title_rect)
    screen.blit(subtitle_image, subtitle_rect)
    screen.blit(play_image, play_rect)
    screen.blit(scores_image, scores_rect)

    pygame.display.flip()


def display_high_scores(ai_settings, screen):

    highscores = get_highscores()
    screen_rect = screen.get_rect()

    screen.fill(ai_settings.menu_bg_color)

    text_white = (255, 255, 255)
    text_green = (0, 255, 0)
    font = pygame.font.SysFont(None, ai_settings.menu_font_size)

    title = "HIGH SCORES"
    back = "PRESS [Q] TO RETURN TO MENU"

    score1 = str(highscores[0])
    score2 = str(highscores[1])
    score3 = str(highscores[2])
    score4 = str(highscores[3])
    score5 = str(highscores[4])

    title_image = font.render(title, True, text_green, ai_settings.menu_bg_color)
    back_image = font.render(back, True, text_green, ai_settings.menu_bg_color)
    score1_img = font.render(score1, True, text_white, ai_settings.menu_bg_color)
    score2_img = font.render(score2, True, text_white, ai_settings.menu_bg_color)
    score3_img = font.render(score3, True, text_white, ai_settings.menu_bg_color)
    score4_img = font.render(score4, True, text_white, ai_settings.menu_bg_color)
    score5_img = font.render(score5, True, text_white, ai_settings.menu_bg_color)

    title_rect = title_image.get_rect()
    back_rect = back_image.get_rect()
    score1_rect = score1_img.get_rect()
    score2_rect = score2_img.get_rect()
    score3_rect = score3_img.get_rect()
    score4_rect = score4_img.get_rect()
    score5_rect = score5_img.get_rect()

    title_rect.centerx = screen_rect.centerx
    title_rect.centery = 50

    back_rect.centerx = screen_rect.centerx
    back_rect.centery = screen_rect.bottom - 50

    score1_rect.centerx = screen_rect.centerx
    score1_rect.centery = 100

    score2_rect.centerx = screen_rect.centerx
    score2_rect.centery = score1_rect.centery + 50

    score3_rect.centerx = screen_rect.centerx
    score3_rect.centery = score2_rect.centery + 50

    score4_rect.centerx = screen_rect.centerx
    score4_rect.centery = score3_rect.centery + 50

    score5_rect.centerx = screen_rect.centerx
    score5_rect.centery = score4_rect.centery + 50

    screen.blit(title_image, title_rect)
    screen.blit(back_image, back_rect)
    screen.blit(score1_img, score1_rect)
    screen.blit(score2_img, score2_rect)
    screen.blit(score3_img, score3_rect)
    screen.blit(score4_img, score4_rect)
    screen.blit(score5_img, score5_rect)

    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets"""
    # Update bullet positions
    bullets.update()
    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.player_score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Start a new lvl if fleet is destroyed
        bullets.empty()
        ai_settings.increase_speed()

        # Inc level
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Respond to the ship being hit by an alien"""
    if stats.ships_left > 0:
        # Decrement ships left
        stats.ships_left -= 1

        # Update scoreboard
        sb.prep_ships()

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        rank_score(stats)
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """
    Check if the fleet is at an edge,
    Update the positions of all aliens in the fleet
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
    # Look for aliens hitting bottom of screen
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # Create an alien and place it in the row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 1.25 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1.25 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    # Create an alien and find the number of aliens in a row
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_high_score(stats, sb):
    """Check to see if there's a new high score"""
    if stats.player_score > stats.high_score:
        stats.high_score = stats.player_score
        sb.prep_high_score()


def rank_score(stats):
    score_list = get_highscores()
    score_list.append(stats.player_score)
    score_list.sort(reverse=True)

    score_file = open("highscores.txt", "w")

    for i in range(5):
        score_file.writelines(str(score_list[i]) + '\n')

    score_file.close()


def get_highscores():
    """Open a reference to scoresheet"""
    score_file = open("highscores.txt")
    score_list = []
    for line in score_file:
        score_list.append(int(line[:-1]))

    score_file.close()

    score_list.sort(reverse=True)

    return score_list
