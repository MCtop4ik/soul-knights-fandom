import random

import pygame

from assets import Assets
from settings.constants import Constants
from sprites.box_structures import BoxStructures
from sprites.map_sprites.box import Box
from sprites.map_sprites.door import Door
from sprites.map_sprites.wall import Wall
from sprites.sprite_groups import SpriteGroups


class CameraGroup(pygame.sprite.Group):

    def __init__(self, width, height, lvl):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.width, self.height = width, height

        self.map = lvl
        self.assets = Assets()
        self.constants = Constants()

        self.offset = pygame.math.Vector2()
        self.quadrant_size = Constants().quadrant_size
        self.empty_cell = Constants().EMPTY_CELL
        self.road_cell = Constants().ROAD_CELL
        self.screen_size = Constants().screen_size

        self.half_w = self.width // 2
        self.half_h = self.height // 2

    def map_draw(self):
        from level import Level
        Level().screen.fill((0, 0, 0))
        player_offset_y = (SpriteGroups().player.rect.centery // self.quadrant_size)
        player_offset_x = (SpriteGroups().player.rect.centerx // self.quadrant_size)
        screen_limit_y = (self.screen_size[1] // self.quadrant_size)
        screen_limit_x = (self.screen_size[0] // self.quadrant_size)
        half_screen_limit_y = round(screen_limit_y / 2)
        half_screen_limit_x = round(screen_limit_x / 2)
        offset_i = player_offset_y - half_screen_limit_y - 2
        offset_j = player_offset_x - half_screen_limit_x - 2
        limit_i = screen_limit_y + 4
        limit_j = screen_limit_x + 4
        for i in range(
                offset_i,
                offset_i + limit_i if offset_i + limit_i < len(self.map) else len(self.map)):
            for j in range(
                    offset_j,
                    offset_j + limit_j if offset_j + limit_j < len(self.map[0]) else len(self.map[0])):
                div = self.map[i][j]
                if div != self.constants.EMPTY_CELL:
                    ground_surf = self.assets.images[div.asset_abbr]
                    self.display_surface.blit(
                        ground_surf,
                        (self.quadrant_size * j, self.quadrant_size * i) - self.offset)

    def wall_draw(self):
        walls_group = SpriteGroups().walls_group
        doors_group = SpriteGroups().doors_group
        for i in range(1, len(self.map) - 1):
            for j in range(1, len(self.map[0]) - 1):
                div = self.map[i][j]
                cells_around = (self.map[i + 1][j], self.map[i - 1][j], self.map[i][j + 1], self.map[i][j - 1])
                diagonal_cells = (self.map[i + 1][j + 1], self.map[i - 1][j - 1],
                                  self.map[i - 1][j + 1], self.map[i + 1][j - 1])
                if div != self.empty_cell and self.empty_cell in cells_around:
                    Wall(
                        (self.quadrant_size * j + self.quadrant_size // 2,
                         self.quadrant_size * i + self.quadrant_size // 2),
                        walls_group)
                if div != self.empty_cell and self.road_cell.name in \
                        list(map(lambda cell: cell.name, cells_around)) and \
                        div.name != self.road_cell.name:
                    if len(list(filter(
                            lambda x: x.name == self.road_cell.name and x != self.empty_cell,
                            cells_around + diagonal_cells
                    ))) == 2:
                        Wall(
                            (self.quadrant_size * j + self.quadrant_size // 2,
                             self.quadrant_size * i + self.quadrant_size // 2),
                            walls_group)
                    else:
                        Door(
                            (self.quadrant_size * j + self.quadrant_size // 2,
                             self.quadrant_size * i + self.quadrant_size // 2),
                            doors_group)

    def box_draw(self, enemy_coordinates, enemy_room_sizes):
        boxes_group = SpriteGroups().boxes_group
        for enemy_coordinate, room_size in zip(enemy_coordinates, enemy_room_sizes):
            ec_x = (enemy_coordinate[1] * self.constants.quadrant_size *
                    self.constants.big_cell_size +
                    (self.constants.quadrant_size * self.constants.big_cell_size) // 2)
            ec_y = (enemy_coordinate[0] * self.constants.quadrant_size *
                    self.constants.big_cell_size +
                    (self.constants.quadrant_size * self.constants.big_cell_size) // 2)
            max_offset_x = (room_size[1] // 2 - 4) * self.constants.quadrant_size
            max_offset_y = (room_size[0] // 2 - 4) * self.constants.quadrant_size
            min_amount_of_boxes = random.randint(3, 7)
            cnt = 0
            while cnt < min_amount_of_boxes:
                for i in range(ec_y - max_offset_y, ec_y + max_offset_y, self.constants.quadrant_size):
                    for j in range(ec_x - max_offset_x, ec_x + max_offset_x, self.constants.quadrant_size):
                        box_spawn_chance = 5
                        if random.randint(1, box_spawn_chance) == random.randint(1, 10):
                            box_structure = BoxStructures().random_box_structure()
                            for box_i in range(len(box_structure)):
                                for box_j in range(len(box_structure[0])):
                                    box_x, box_y = (self.quadrant_size * box_j + j + self.quadrant_size // 2,
                                                    self.quadrant_size * box_i + i + self.quadrant_size // 2)
                                    cells_around = (self.map[i // self.quadrant_size + 1][j // self.quadrant_size],
                                                    self.map[i // self.quadrant_size - 1][j // self.quadrant_size],
                                                    self.map[i // self.quadrant_size][j // self.quadrant_size + 1],
                                                    self.map[i // self.quadrant_size][j // self.quadrant_size - 1])
                                    if self.empty_cell not in cells_around:
                                        Box((box_x, box_y), boxes_group)
                                        cnt += 1

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def draw_sprites(self, sprite_for_camera):
        sprite_groups = SpriteGroups()
        self.center_target_camera(sprite_for_camera)
        self.map_draw()
        for sprite in sorted(
                self.sprites() +
                sprite_groups.walls_group.sprites() +
                sprite_groups.doors_group.sprites() +
                sprite_groups.boxes_group.sprites() +
                sprite_groups.portal_group.sprites() +
                sprite_groups.chests_group.sprites() +
                sprite_groups.enemies_group.sprites() +
                sprite_groups.bullets_group.sprites(),
                key=lambda x: x.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
