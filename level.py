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
from sprites.inventory import InventoryArmorSprite, InventoryPocketSprite


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
        inventory_armor_sprite = InventoryArmorSprite((Constants().screen_size[1] - Constants().quadrant_size,
                                                       Constants().screen_size[0] - Constants().quadrant_size),
                                                      SpriteGroups().inventory_armor_group)

        # pocket sprites
        inventory_pocket_0_sprite = InventoryPocketSprite((Constants().screen_size[1] - 9 * Constants().quadrant_size,
                                                           Constants().screen_size[0] - Constants().quadrant_size),
                                                          SpriteGroups().inventory_pocket_group)
        inventory_pocket_1_sprite = InventoryPocketSprite(
            (Constants().screen_size[1] - 8 * Constants().quadrant_size + (1 * 15),
             Constants().screen_size[0] - Constants().quadrant_size),
            SpriteGroups().inventory_pocket_group)

        inventory_pocket_2_sprite = InventoryPocketSprite(
            (Constants().screen_size[1] - 7 * Constants().quadrant_size + (2 * 15),
             Constants().screen_size[0] - Constants().quadrant_size),
            SpriteGroups().inventory_pocket_group)

        inventory_pocket_3_sprite = InventoryPocketSprite(
            (Constants().screen_size[1] - 6 * Constants().quadrant_size + (3 * 15),
             Constants().screen_size[0] - Constants().quadrant_size),
            SpriteGroups().inventory_pocket_group)

        inventory_pocket_4_sprite = InventoryPocketSprite(
            (Constants().screen_size[1] - 5 * Constants().quadrant_size + (4 * 15),
             Constants().screen_size[0] - Constants().quadrant_size),
            SpriteGroups().inventory_pocket_group)

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
            self.screen.blit(inventory_armor_sprite.image, inventory_armor_sprite.rect)
            self.screen.blit(inventory_pocket_0_sprite.image, inventory_pocket_0_sprite.rect)
            self.screen.blit(inventory_pocket_1_sprite.image, inventory_pocket_1_sprite.rect)
            self.screen.blit(inventory_pocket_2_sprite.image, inventory_pocket_2_sprite.rect)
            self.screen.blit(inventory_pocket_3_sprite.image, inventory_pocket_3_sprite.rect)
            self.screen.blit(inventory_pocket_4_sprite.image, inventory_pocket_4_sprite.rect)




            pygame.display.update()
            clock.tick(60)
