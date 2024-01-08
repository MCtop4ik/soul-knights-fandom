import sys

import pygame

from camera import CameraGroup
from map_generation.create_field_matrix import CreateFieldMatrix
from patterns.creational_patterns.singleton import Singleton
from settings.constants import Constants
from sprites.map_sprites.chest import Chest
from sprites.map_sprites.portal import Portal
from sprites.player import Player
from sprites.sprite_groups import SpriteGroups
from sprites.inventory import InventorySprite


class Level(metaclass=Singleton):

    def __init__(self):
        self.screen = pygame.display.set_mode(Constants().screen_size)

    def start(self):
        clock = pygame.time.Clock()
        level, \
        start_coordinates, \
        portal_coordinates, \
        treasure_room_coordinates = CreateFieldMatrix().generate_field()
        SpriteGroups().camera_group = CameraGroup(*Constants().camera_size, level)
        SpriteGroups().player = Player(
            (start_coordinates[1] * Constants().quadrant_size * Constants().big_cell_size +
             (Constants().quadrant_size * Constants().big_cell_size) // 2,
             start_coordinates[0] * Constants().quadrant_size * Constants().big_cell_size +
             (Constants().quadrant_size * Constants().big_cell_size) // 2),
            Constants().player_size,
            SpriteGroups().camera_group)
        SpriteGroups().camera_group.wall_draw()
        Portal(
            (portal_coordinates[1] * Constants().quadrant_size * Constants().big_cell_size +
             (Constants().quadrant_size * Constants().big_cell_size) // 2,
             portal_coordinates[0] * Constants().quadrant_size * Constants().big_cell_size +
             (Constants().quadrant_size * Constants().big_cell_size) // 2),
            SpriteGroups().portal_group)
        for treasure_room_coordinate in treasure_room_coordinates:
            trc_x = treasure_room_coordinate[0]
            trc_y = treasure_room_coordinate[1]
            Chest(
                (trc_y * Constants().quadrant_size * Constants().big_cell_size +
                 (Constants().quadrant_size * Constants().big_cell_size) // 2,
                 trc_x * Constants().quadrant_size * Constants().big_cell_size +
                 (Constants().quadrant_size * Constants().big_cell_size) // 2),
                SpriteGroups().chests_group)
        inventory_sprite = InventorySprite((Constants().screen_size[1] - Constants().quadrant_size,
                                            Constants().screen_size[0] - Constants().quadrant_size),
                                           SpriteGroups().inventory_group)
        self.screen.blit(inventory_sprite.image, inventory_sprite.rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            SpriteGroups().camera_group.update()
            # SpriteGroups().walls_group.update()
            SpriteGroups().doors_group.update()
            SpriteGroups().chests_group.update()
            SpriteGroups().portal_group.update()
            SpriteGroups().camera_group.draw_sprites(SpriteGroups().player)

            pygame.display.update()
            clock.tick(60)
