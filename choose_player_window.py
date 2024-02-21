import pygame
import sys

import starting_window


def choose_player():
    pygame.init()
    window_width = 400
    window_height = 300
    cell_width = window_width // 4
    cell_height = window_height // 3
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Player Selection")
    player_images = {
        "Player 1": pygame.image.load("assets/images_test/characters/mage_4_0.png").convert_alpha(),
        "Player 2": pygame.image.load("assets/images_test/characters/mage_4_0.png").convert_alpha(),
        "Player 3": pygame.image.load("assets/images_test/characters/mage_4_0.png").convert_alpha(),
        "Player 4": pygame.image.load("assets/images_test/characters/mage_4_0.png").convert_alpha(),
        "Player 5": pygame.image.load("assets/images_test/characters/mage_4_0.png").convert_alpha(),
        "Player 6": pygame.image.load("assets/images_test/characters/mage_4_0.png").convert_alpha(),
        "Player 7": pygame.image.load("assets/images_test/characters/mage_4_0.png").convert_alpha(),
        "Player 8": pygame.image.load("assets/images_test/characters/mage_4_0.png").convert_alpha(),
        "Player 9": pygame.image.load("assets/images_test/characters/mage_4_0.png").convert_alpha(),
        "Player 10": pygame.image.load("assets/images_test/characters/mage_4_0.png").convert_alpha(),
        "Player 11": pygame.image.load("assets/images_test/characters/mage_4_0.png").convert_alpha(),
        "Player 12": pygame.image.load("assets/images_test/characters/mage_4_0.png").convert_alpha()
    }

    font = pygame.font.Font(None, 24)

    selected_row = 0
    selected_col = 0

    def draw_player_buttons():
        for num, (player, image) in enumerate(player_images.items()):
            row = num // 4
            col = num % 4
            x = col * cell_width
            y = row * cell_height
            button_rect = pygame.Rect(x, y, cell_width, cell_height)
            pygame.draw.rect(window, (255, 255, 255), button_rect)
            window.blit(image, button_rect)
            if row == selected_row and col == selected_col:
                pygame.draw.rect(window, (255, 0, 0), button_rect, 2)
            text_surface = font.render(player, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=button_rect.center)
            window.blit(text_surface, text_rect)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_row = max(0, selected_row - 1)
                elif event.key == pygame.K_DOWN:
                    selected_row = min(2, selected_row + 1)
                elif event.key == pygame.K_LEFT:
                    selected_col = max(0, selected_col - 1)
                elif event.key == pygame.K_RIGHT:
                    selected_col = min(3, selected_col + 1)
                elif event.key == pygame.K_RETURN:
                    selected_player = list(player_images.keys())[selected_row * 4 + selected_col]
                    print(f"Selected player: {selected_player}")
                    pygame.quit()
                    starting_window.starting_window()
                    sys.exit()

        window.fill((255, 255, 255))
        draw_player_buttons()
        pygame.display.flip()
