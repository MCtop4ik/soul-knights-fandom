import os
import sys
import pygame
from assets import Assets
from settings.statistics import Statistics
from sprites.sprite_groups import SpriteGroups
from windows.choose_player_window import ChoosePlayerWindow
from windows.settings_window import SettingsMenu


class StartWindow:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(True)
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 400, 300
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Starting Window")
        os.environ['SDL_VIDEO_WINDOW_POS'] = '200,100'
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.font = pygame.font.Font(None, 36)
        self.bg = Assets().load_image_with_size('start_background.jpg',
                                                (self.WINDOW_WIDTH + 100, self.WINDOW_HEIGHT + 100))

    def draw_text(self, text, color, x, y):
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.screen.blit(textobj, textrect)

    def start_game(self):
        from level import Level
        from map_generation.room_factory import RoomFactory
        from settings.constants import Constants
        from settings.player_state import PlayerState
        pygame.display.set_caption("Main window")
        PlayerState().health = PlayerState().max_health
        PlayerState().energy = PlayerState().max_energy
        PlayerState().money = 0
        PlayerState().level_index = 0
        SpriteGroups().clear_level_sprites()
        Statistics().clear()
        Constants().name = PlayerState().levels[PlayerState().level_index]
        RoomFactory(Constants().name).load_assets()
        Level().start()

    def choose_player(self):
        ChoosePlayerWindow().run()

    def settings(self):
        settings_menu = SettingsMenu()
        settings_menu.run()

    def run(self):
        pygame.mixer.music.stop()
        while True:
            self.screen.fill(self.WHITE)
            self.screen.blit(self.bg, (0, 0))
            self.draw_text("Start Game", self.WHITE, 148, 70)
            self.draw_text("Choose Player", self.WHITE, 148, 150)
            self.draw_text("Settings", self.WHITE, 148, 224)
            start_button = pygame.Rect(65, 60, 300, 55)
            choose_button = pygame.Rect(65, 135, 300, 55)
            settings_button = pygame.Rect(65, 200, 300, 55)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if start_button.collidepoint(mouse_pos):
                        self.start_game()
                    elif choose_button.collidepoint(mouse_pos):
                        self.choose_player()
                    elif settings_button.collidepoint(mouse_pos):
                        self.settings()
            pygame.display.update()
