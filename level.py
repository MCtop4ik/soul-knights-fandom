import random
import sys

import pygame

from camera import CameraGroup
from map_generation.create_field_matrix import CreateFieldMatrix
from patterns.creational_patterns.singleton import Singleton
from settings.constants import Constants
from sprites.enemy import Enemy
from sprites.enemy_list import EnemyList
from sprites.inventory import InventoryV2
from sprites.inventory_sprite import InventorySpriteV2
from sprites.map_sprites.chest import Chest
from sprites.map_sprites.portal import Portal
from sprites.player import Player
from sprites.sprite_groups import SpriteGroups
from sprites.item_sprites.weapon import Weapon
from sprites.weapons_list import WeaponsList


class Level(metaclass=Singleton):

    def __init__(self):
        self.screen = pygame.display.set_mode(Constants().screen_size)
        self.constants = Constants()

    def start(self):
        clock = pygame.time.Clock()
        fps = self.constants.FPS
        pygame.mixer.init()
        level, \
            start_coordinates, \
            portal_coordinates, \
            treasure_room_coordinates, \
            enemy_coordinates, \
            enemy_room_sizes = CreateFieldMatrix().generate_field()
        WeaponsList().add_weapons_to_list()
        WeaponsList().add_bullets_to_list()
        EnemyList().add_enemies_to_list()
        InventoryV2().add_item_in_inventory(WeaponsList().weapons_list[0])
        InventoryV2().add_item_in_inventory(WeaponsList().weapons_list[1])
        InventoryV2().add_item_in_inventory(WeaponsList().weapons_list[1])
        SpriteGroups().camera_group = CameraGroup(*self.constants.camera_size, level)
        SpriteGroups().player = Player(
            (start_coordinates[1] * self.constants.quadrant_size * self.constants.big_cell_size +
             (self.constants.quadrant_size * self.constants.big_cell_size) // 2,
             start_coordinates[0] * self.constants.quadrant_size * self.constants.big_cell_size +
             (self.constants.quadrant_size * self.constants.big_cell_size) // 2),
            self.constants.player_size,
            SpriteGroups().camera_group)
        SpriteGroups().weapon = Weapon(
            (start_coordinates[1] * self.constants.quadrant_size * self.constants.big_cell_size +
             (self.constants.quadrant_size * self.constants.big_cell_size) // 2,
             start_coordinates[0] * self.constants.quadrant_size * self.constants.big_cell_size +
             (self.constants.quadrant_size * self.constants.big_cell_size) // 2),
            SpriteGroups().camera_group)
        SpriteGroups().camera_group.wall_draw()
        Portal(
            (portal_coordinates[1] * self.constants.quadrant_size * self.constants.big_cell_size +
             (self.constants.quadrant_size * self.constants.big_cell_size) // 2,
             portal_coordinates[0] * self.constants.quadrant_size * self.constants.big_cell_size +
             (self.constants.quadrant_size * self.constants.big_cell_size) // 2),
            SpriteGroups().portal_group)
        for treasure_room_coordinate in treasure_room_coordinates:
            trc_x = treasure_room_coordinate[0]
            trc_y = treasure_room_coordinate[1]
            Chest(
                (trc_y * self.constants.quadrant_size * self.constants.big_cell_size +
                 (self.constants.quadrant_size * self.constants.big_cell_size) // 2,
                 trc_x * self.constants.quadrant_size * self.constants.big_cell_size +
                 (self.constants.quadrant_size * self.constants.big_cell_size) // 2),
                SpriteGroups().chests_group)

        uncleared_rooms = []
        for enemy_coordinate, room_size in zip(enemy_coordinates, enemy_room_sizes):
            ec_x = enemy_coordinate[1]
            ec_y = enemy_coordinate[0]
            max_offset = (room_size[0] // 2 - 4) * self.constants.quadrant_size
            enemy_amount = random.randint(
                self.constants.min_enemy_amount,
                self.constants.max_enemy_amount)
            uncleared_rooms.append((ec_x, ec_y, enemy_amount))
            for _ in range(enemy_amount):
                Enemy(EnemyList().get_random_enemy(),
                      (ec_x * self.constants.quadrant_size * self.constants.big_cell_size +
                          (self.constants.quadrant_size * self.constants.big_cell_size) // 2
                          + random.randint(-max_offset, max_offset),
                          ec_y * self.constants.quadrant_size * self.constants.big_cell_size +
                          (self.constants.quadrant_size * self.constants.big_cell_size) // 2
                          + random.randint(-max_offset, max_offset)),
                      (ec_x, ec_y),
                      SpriteGroups().enemies_group)
        SpriteGroups().player.set_uncleared_rooms(uncleared_rooms)

        InventorySpriteV2((self.constants.screen_size[1] - self.constants.quadrant_size,
                           self.constants.screen_size[0] - self.constants.quadrant_size),
                          SpriteGroups().inventory_group)
        pygame.mixer.music.load('assets/music/FallingMysts.mp3')
        pygame.mixer.music.play()

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
            SpriteGroups().walls_group.update()
            SpriteGroups().doors_group.update()
            SpriteGroups().chests_group.update()
            SpriteGroups().portal_group.update()
            SpriteGroups().bullets_group.update()
            SpriteGroups().enemies_group.update()
            SpriteGroups().inventory_group.update()
            SpriteGroups().camera_group.draw_sprites(SpriteGroups().player)
            for inventory_cell in SpriteGroups().inventory_group.sprites():
                self.screen.blit(inventory_cell.image, inventory_cell.rect)

            pygame.display.update()
            clock.tick(fps)
