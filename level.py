import sys

import pygame

from camera import CameraGroup
from map_generation.create_field_matrix import CreateFieldMatrix
from map_generation.room_factory import RoomFactory
from patterns.creational_patterns.singleton import Singleton
from settings.constants import Constants
from settings.game_state_manager import GameStateManager
from sprites.map_sprites.portal import Portal
from sprites.player import Player
from sprites.sprite_groups import SpriteGroups


class Level(metaclass=Singleton):

    def __init__(self):
        self.screen = pygame.display.set_mode(Constants().screen_size)

    def start(self):
        clock = pygame.time.Clock()
        level, start_coordinates, portal_coordinates = CreateFieldMatrix().generate_field()
        camera_group = CameraGroup(*Constants().camera_size, level)
        player = Player(
            (start_coordinates[1] * Constants().quadrant_size * Constants().big_cell_size +
             (Constants().quadrant_size * Constants().big_cell_size) // 2,
             start_coordinates[0] * Constants().quadrant_size * Constants().big_cell_size +
             (Constants().quadrant_size * Constants().big_cell_size) // 2),
            Constants().player_size,
            camera_group)
        camera_group.wall_draw()
        Portal(
            (portal_coordinates[1] * Constants().quadrant_size * Constants().big_cell_size +
             (Constants().quadrant_size * Constants().big_cell_size) // 2,
             portal_coordinates[0] * Constants().quadrant_size * Constants().big_cell_size +
             (Constants().quadrant_size * Constants().big_cell_size) // 2),
            SpriteGroups().portal_group)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            if GameStateManager().next_level:
                GameStateManager().next_level = False
                Constants().name = "1"
                SpriteGroups().doors_group = pygame.sprite.Group()
                SpriteGroups().walls_group = pygame.sprite.Group()
                SpriteGroups().portal_group = pygame.sprite.Group()
                RoomFactory(Constants().name).load_assets()
                self.start()

            camera_group.update()
            camera_group.draw_sprites(player)

            pygame.display.update()
            clock.tick(60)
