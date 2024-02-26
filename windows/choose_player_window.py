import pygame
import sys

from assets import Assets
from logger import CustomLogger
from settings.player_state import PlayerState


class ChoosePlayerWindow:
    def __init__(self):
        pygame.init()
        self.window_width = 400
        self.window_height = 300
        self.cell_width = self.window_width // 4
        self.cell_height = self.window_height // 3
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Player Selection")
        self.assets = Assets
        self.image_path = 'assets/images_test/characters/'
        self.name_to_sprite_name = {
            "Player 1": "mage_4_0",
            "Player 2": "mage_17_0",
            "Player 3": "mage_4_0",
            "Player 4": "mage_17_0",
            "Player 5": "mage_4_0",
            "Player 6": "mage_17_0",
            "Player 7": "mage_4_0",
            "Player 8": "mage_17_0",
            "Player 9": "mage_4_0",
            "Player 10": "mage_17_0",
            "Player 11": "mage_4_0",
            "Player 12": "mage_17_0"
        }
        self.player_images = {}
        self.load_player_images()

        self.font = pygame.font.Font(None, 24)
        self.selected_row = 0
        self.selected_col = 0

    def load_player_images(self):
        for key, img_name in self.name_to_sprite_name.items():
            self.player_images[key] = self.assets.load_alpha_image(self.image_path + img_name + '.png')

    def draw_player_buttons(self):
        for num, (player, image) in enumerate(self.player_images.items()):
            row = num // 4
            col = num % 4
            x = col * self.cell_width
            y = row * self.cell_height
            button_rect = pygame.Rect(x, y, self.cell_width, self.cell_height)
            pygame.draw.rect(self.window, (255, 255, 255), button_rect)
            self.window.blit(image, button_rect)
            if row == self.selected_row and col == self.selected_col:
                pygame.draw.rect(self.window, (255, 0, 0), button_rect, 2)
            text_surface = self.font.render(player, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=button_rect.center)
            self.window.blit(text_surface, text_rect)

    def run(self):
        from windows.starting_window import StartWindow
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    StartWindow().run()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_row = max(0, self.selected_row - 1)
                    elif event.key == pygame.K_DOWN:
                        self.selected_row = min(2, self.selected_row + 1)
                    elif event.key == pygame.K_LEFT:
                        self.selected_col = max(0, self.selected_col - 1)
                    elif event.key == pygame.K_RIGHT:
                        self.selected_col = min(3, self.selected_col + 1)
                    elif event.key == pygame.K_RETURN:
                        selected_player = list(self.player_images.keys())[self.selected_row * 4 + self.selected_col]
                        CustomLogger().debug(f"Selected player: {selected_player}")
                        new_character = self.name_to_sprite_name[selected_player]
                        PlayerState().character = new_character[:new_character.rfind('_')]
                        pygame.quit()
                        StartWindow().run()
                        sys.exit()

            self.window.fill((255, 255, 255))
            self.draw_player_buttons()
            pygame.display.flip()


if __name__ == "__main__":
    ChoosePlayerWindow().run()
