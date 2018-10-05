import pygame
import pygame.sprite

def build_map(str, img, settings, screen, walls):

    block_image = pygame.image.load('images/map_block.png')
    block_rect = block_image.get_rect()
    screen_rect = screen.get_rect()

    pos_x = 0
    pos_y = 0
    for element in str:
        if element == 'X':
            # Draw the square at (pos_x, pos_y)

        elif element == '.':
            # Draw a dot at (pos_x, pos_y)
        elif element == '\n':
            # If newline, move down to the next row
            pos_y += settings.map_delta_y
            pos_x = 0

        # Increment to next block
        pos_x += settings.map_delta_x

        