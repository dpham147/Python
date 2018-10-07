import sys
import random
from time import sleep
import pygame
import pygame.font
from bullet import Bullet
from alien_bullet import Alien_Bullet
from alien import Alien
from ufo import UFO
from bunker import Bunker


def check_keydown_events(event, ai_settings, screen, stats, sb, ship, bunkers, aliens, bullets, alien_bullets, audio):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets, audio)
    elif event.key == pygame.K_s and ai_settings.show_menu:
        ai_settings.show_menu = False
        ai_settings.show_game = True
        start_game(ai_settings, screen, stats, sb, ship, bunkers, aliens, bullets, alien_bullets)
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


def fire_bullet(ai_settings, screen, ship, bullets, audio):
    """Fire a bullet if limit not reached yet"""
    # Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        audio.play_laser()


def alien_fire(ai_settings, screen, aliens, alien_bullets):
    """if pygame.time.get_ticks() % ai_settings.fire_rate == 0:
        for alien in aliens:
            fire = random.randint(0, 7)
            if fire == 0:
                new_bullet = Alien_Bullet(ai_settings, screen, alien)
                alien_bullets.add(new_bullet)"""
    for alien in aliens:
        fire = random.randint(0, int(ai_settings.alien_fire_rate))
        if fire == 0:
            new_bullet = Alien_Bullet(ai_settings, screen, alien)
            alien_bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, bunkers, aliens, bullets, alien_bullets, laser):
    """Respond to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #    mouse_x, mouse_y = pygame.mouse.get_pos()
        #    check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, ship, bunkers, aliens, bullets, alien_bullets, laser)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def start_game(ai_settings, screen, stats, sb, ship, bunkers, aliens, bullets, alien_bullets):
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
    bunkers.empty()
    alien_bullets.empty()

    # Redraw bunkers
    setup_bunkers(screen, ship, bunkers)
        
    # Create a new fleet and center ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, bunkers, alien_bullets, ufo):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.game_bg_color)

    # Chance to spawn ufo
    spawn_ufo(ai_settings, screen, ufo)

    # Redraw all bullets behind ship and aliens.
    bullets.draw(screen)
    alien_bullets.draw(screen)
    alien_fire(ai_settings, screen, aliens, alien_bullets)

    ship.blitme()
    bunkers.draw(screen)
    aliens.draw(screen)
    ufo.draw(screen)
    show_ufo_score(screen, ai_settings)

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
    audio = "GAME OVER"
    audio_img = font.render(audio, True, (0, 255, 0), ai_settings.game_bg_color)
    audio_rect = audio_img.get_rect()
    audio_rect.centerx = screen_rect.centerx
    audio_rect.centery = screen_rect.centery
    screen.blit(audio_img, audio_rect)

    audio = "PRESS [Q] TO RETURN TO MENU"
    audio_img = font.render(audio, True, (0, 255, 0), ai_settings.game_bg_color)
    audio_rect = audio_img.get_rect()
    audio_rect.centerx = screen_rect.centerx
    audio_rect.centery = screen_rect.centery + 40
    screen.blit(audio_img, audio_rect)


def display_menu(ai_settings, screen):

    screen_rect = screen.get_rect()
    center_screen = screen_rect.centerx

    screen.fill(ai_settings.menu_bg_color)

    # Display Title and Controls

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

    # Display aliens and points
    alien1 = pygame.image.load('images/alien_1.png')
    alien2 = pygame.image.load('images/alien_3.png')
    alien3 = pygame.image.load('images/alien_5.png')
    ufo = pygame.image.load('images/ufo.png')

    pnts1 = str(ai_settings.alien_points_1) + ' POINTS'
    pnts2 = str(ai_settings.alien_points_2) + ' POINTS'
    pnts3 = str(ai_settings.alien_points_3) + ' POINTS'
    ufo_pnts = str(ai_settings.ufo_points) + ' POINTS'

    pnts1_img = menu_font.render(pnts1, True, white_color, ai_settings.menu_bg_color)
    pnts2_img = menu_font.render(pnts2, True, white_color, ai_settings.menu_bg_color)
    pnts3_img = menu_font.render(pnts3, True, white_color, ai_settings.menu_bg_color)
    ufo_points_img = menu_font.render(ufo_pnts, True, white_color, ai_settings.menu_bg_color)

    alien_rect1 = alien1.get_rect()
    alien_rect2 = alien2.get_rect()
    alien_rect3 = alien3.get_rect()
    ufo_rect = ufo.get_rect()

    pnts1_rect = pnts1_img.get_rect()
    pnts2_rect = pnts2_img.get_rect()
    pnts3_rect = pnts3_img.get_rect()
    ufo_points_rect = ufo_points_img.get_rect()

    alien_rect2.centerx = screen_rect.centerx - 100
    alien_rect2.centery = screen_rect.centery
    pnts2_rect.left = screen_rect.centerx
    pnts2_rect.centery = alien_rect2.centery

    alien_rect1.centerx = screen_rect.centerx - 100
    alien_rect1.centery = alien_rect2.centery - 50
    pnts1_rect.left = screen_rect.centerx
    pnts1_rect.centery = alien_rect1.centery

    alien_rect3.centerx = screen_rect.centerx - 100
    alien_rect3.centery = alien_rect2.centery + 50
    pnts3_rect.left = screen_rect.centerx
    pnts3_rect.centery = alien_rect3.centery

    ufo_rect.centerx = screen_rect.centerx - 100
    ufo_rect.centery = alien_rect1.centery - 50
    ufo_points_rect.centerx = screen_rect.centerx + 100
    ufo_points_rect.centery = ufo_rect.centery

    # Blit images

    screen.blit(title_image, title_rect)
    screen.blit(subtitle_image, subtitle_rect)
    screen.blit(play_image, play_rect)
    screen.blit(scores_image, scores_rect)
    screen.blit(alien1, alien_rect1)
    screen.blit(alien2, alien_rect2)
    screen.blit(alien3, alien_rect3)
    screen.blit(ufo, ufo_rect)
    screen.blit(pnts1_img, pnts1_rect)
    screen.blit(pnts2_img, pnts2_rect)
    screen.blit(pnts3_img, pnts3_rect)
    screen.blit(ufo_points_img, ufo_points_rect)

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


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, bunkers, alien_bullets, ufo, audio):
    """Update position of bullets and get rid of old bullets"""
    screen_rect = screen.get_rect()
    # Update bullet positions
    bullets.update()
    alien_bullets.update()
    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for abullet in alien_bullets.copy():
        if abullet.rect.top >= screen_rect.bottom:
            alien_bullets.remove(abullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, ufo)
    check_bullet_ship_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, audio)
    check_bullet_bunker_collisions(screen, bullets, bunkers, alien_bullets)
    check_bullet_ufo_collisions(screen, ai_settings, stats, sb, ufo, bullets)


def check_bullet_ship_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, audio):
    if pygame.sprite.spritecollide(ship, alien_bullets, True):
        ship.destroy()
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets, alien_bullets, audio)


def check_bullet_ufo_collisions(screen, ai_settings, stats, sb, ufo, bullets):
    collisions = pygame.sprite.groupcollide(ufo, bullets, True, True)
    if collisions:
        for _ufo in collisions:
            points = ai_settings.ufo_points
            stats.player_score += points
            sb.prep_score()
            check_high_score(stats, sb)
            ai_settings.ufo_show_score = True
            ai_settings.ufo_score_center = _ufo.rect.center
            print(ai_settings.ufo_score_center)


def show_ufo_score(screen, ai_settings):
    if ai_settings.ufo_show_score:
        points = ai_settings.ufo_points
        score = str(points)
        font = pygame.font.SysFont(None, ai_settings.menu_font_size)
        score_image = font.render(score, True, (255, 255, 255), ai_settings.game_bg_color)
        score_rect = score_image.get_rect()
        score_rect.center = ai_settings.ufo_score_center
        screen.blit(score_image, score_rect)

        ai_settings.ufo_score_delay -= 1
        if ai_settings.ufo_score_delay == 0:
            ai_settings.ufo_show_score = False
            ai_settings.ufo_score_delay = 500
    

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, ufos):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that collided
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)

    if collisions:
        for alien in collisions:
            if alien.alien_type == 0:
                stats.player_score += ai_settings.alien_points_3
                sb.prep_score()
            elif alien.alien_type == 1:
                stats.player_score += ai_settings.alien_points_2
                sb.prep_score()
            elif alien.alien_type == 2:
                stats.player_score += ai_settings.alien_points_1
                sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Start a new lvl if fleet is destroyed
        bullets.empty()
        alien_bullets.empty()
        ai_settings.increase_speed()

        # Inc level
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def check_bullet_bunker_collisions(screen, bullets, bunkers, alien_bullets):
    for bunker in bunkers:
        if pygame.sprite.spritecollide(bunker, bullets, True):
            bunker.eat()
        if pygame.sprite.spritecollide(bunker, alien_bullets, True):
            bunker.eat()


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


def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets, alien_bullets, audio):
    """Respond to the ship being hit by an alien"""
    if stats.ships_left > 0:
        # Decrement ships left
        stats.ships_left -= 1

        # Update scoreboard
        sb.prep_ships()

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        rank_score(stats)
        pygame.mouse.set_visible(True)
        audio.play_gameover()


def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets, bunkers, alien_bullets, audio):
    """Check if any aliens have reached the bottom of the screen"""
    bunker = bunkers.sprites()[0]
    for alien in aliens.sprites():
        if alien.rect.bottom >= bunker.rect.top:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets, alien_bullets, audio)
            break


def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets, bunkers, alien_bullets, audio):
    """
    Check if the fleet is at an edge,
    Update the positions of all aliens in the fleet
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets, alien_bullets, audio)
    # Look for aliens hitting bottom of screen
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets, bunkers, alien_bullets, audio)


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
    type = row_number % 3

    alien = Alien(ai_settings, screen, type)
    alien_width = alien.rect.width
    alien.x = alien_width + 1.25 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1.25 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    # Create an alien and find the number of aliens in a row
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_settings, screen, 0)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def setup_bunkers(screen, ship, bunkers):
    """Create 4 bunkers on the field"""
    screen_rect = screen.get_rect()
    partition = screen_rect.width / 5

    for bunker_num in range(4):
        bunker = Bunker(screen, ship)
        bunker.rect.centerx = partition * (1 + bunker_num)
        bunkers.add(bunker)


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


def spawn_ufo(ai_settings, screen, ufo):
    if random.randint(0, 1000) == 0 and ai_settings.show_game:
        if len(ufo) == 0:
            ai_settings.ufo_move = True
            newUFO = UFO(ai_settings, screen)
            ufo.add(newUFO)
        else:
            ai_settings.ufo_move = True

