import os
import sys

import pygame

import starting_window
from assets import Assets


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def start_window():
    pygame.init()
    pygame.mouse.set_visible(True)
    WINDOW_WIDTH, WINDOW_HEIGHT = 400, 300
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Starting Window")

    bg = Assets().load_image_with_size('end_background.jpg', (WINDOW_WIDTH, WINDOW_HEIGHT))

    os.environ['SDL_VIDEO_WINDOW_POS'] = '200,100'
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 36)
    while True:
        screen.fill(WHITE)
        screen.blit(bg, (0, 0))

        main_menu_button = pygame.Rect(65, 100, 200, 50)
        # pygame.draw.rect(screen, BLACK, main_menu_button)
        draw_text("Main Menu", font, WHITE, screen, 100, 100)

        exit_button = pygame.Rect(70, 170, 200, 50)
        # pygame.draw.rect(screen, BLACK, exit_button)
        draw_text("Exit", font, WHITE, screen, 130, 200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if main_menu_button.collidepoint(mouse_pos):
                    starting_window.start_window()
                elif exit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    start_window()
