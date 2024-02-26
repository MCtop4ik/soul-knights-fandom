import pygame
import sys


class SettingsMenu:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Settings")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.music_enabled = False
        self.music_volume = 50
        self.music_button_rect = pygame.Rect(100, self.height // 2 - 50, 300, 50)
        self.volume_slider_rect = pygame.Rect(100, self.height // 2 + 50, 300, 20)

    def toggle_music(self):
        self.music_enabled = not self.music_enabled
        # Add code to toggle music playback

    def change_volume(self, value):
        self.music_volume = value
        # Add code to change music volume

    def draw(self):
        self.screen.fill((255, 255, 255))
        text = self.font.render("Settings Menu", True, (0, 0, 0))
        self.screen.blit(text, (self.width // 2 - text.get_width() // 2, 50))

        # Draw music toggle button
        music_text = "Enabled" if self.music_enabled else "Disabled"
        pygame.draw.rect(self.screen, (200, 200, 200), self.music_button_rect)
        music_button_text = self.font.render("Toggle Music: {}".format(music_text), True, (0, 0, 0))
        self.screen.blit(music_button_text, (self.music_button_rect.x + 10, self.music_button_rect.y + 10))

        # Draw volume slider
        pygame.draw.rect(self.screen, (200, 200, 200), self.volume_slider_rect)
        volume_slider_button_rect = pygame.Rect(self.volume_slider_rect.x + self.music_volume * 3,
                                                self.volume_slider_rect.y, 20, 20)
        pygame.draw.rect(self.screen, (0, 0, 0), volume_slider_button_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Check if the mouse click is inside the music toggle button
                    if self.music_button_rect.collidepoint(event.pos):
                        self.toggle_music()
                    # Check if the mouse click is inside the volume slider
                    elif self.volume_slider_rect.collidepoint(event.pos):
                        new_volume = (event.pos[0] - self.volume_slider_rect.x) // 3
                        self.change_volume(new_volume)

    def run(self):
        running = True
        while running:
            self.handle_events()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    settings_menu = SettingsMenu()
    settings_menu.run()
