import os
import sys
import pygame
from assets import Assets
from settings.statistics import Statistics
from windows.starting_window import StartWindow


class EndScreen:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(True)
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 400, 300
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("End Screen")
        self.bg = Assets().load_image_with_size('end_background.jpg', (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        os.environ['SDL_VIDEO_WINDOW_POS'] = '200,100'
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.font = pygame.font.Font(None, 36)

    def draw_text(self, text, x, y):
        textobj = self.font.render(text, 1, self.WHITE)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.screen.blit(textobj, textrect)

    def run(self):
        pygame.mixer.music.stop()
        while True:
            self.screen.fill(self.WHITE)
            self.screen.blit(self.bg, (0, 0))
            self.draw_text("Main Menu", 100, 100)
            self.draw_text(f"Killed enemies: {Statistics().killed_enemies}", 100, 150)
            self.draw_text("Exit", 130, 200)
            main_menu_button = pygame.Rect(65, 100, 200, 50)
            exit_button = pygame.Rect(70, 170, 200, 50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if main_menu_button.collidepoint(mouse_pos):
                        StartWindow().run()
                    elif exit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()


if __name__ == "__main__":
    EndScreen().run()
