import sys

import pygame

import choose_player_window


def start_game():
    from level import Level
    from map_generation.room_factory import RoomFactory
    from settings.constants import Constants
    from settings.player_state import PlayerState
    pygame.init()
    pygame.display.set_caption("Pygame Window")
    PlayerState().health = PlayerState().max_health
    PlayerState().energy = PlayerState().max_energy
    PlayerState().money = 0
    PlayerState().level_index = 0
    Constants().name = PlayerState().levels[PlayerState().level_index]
    RoomFactory(Constants().name).load_assets()
    Level().start()


def choose_player():
    choose_player_window.choose_player()


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
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 36)
    while True:
        screen.fill(WHITE)
        start_button = pygame.Rect(50, 100, 200, 50)
        pygame.draw.rect(screen, BLACK, start_button)
        draw_text("Start Game", font, WHITE, screen, 65, 110)

        choose_button = pygame.Rect(50, 200, 200, 50)
        pygame.draw.rect(screen, BLACK, choose_button)
        draw_text("Choose Player", font, WHITE, screen, 65, 210)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if start_button.collidepoint(mouse_pos):
                    start_game()
                elif choose_button.collidepoint(mouse_pos):
                    choose_player()

        pygame.display.update()


if __name__ == "__main__":
    start_window()
