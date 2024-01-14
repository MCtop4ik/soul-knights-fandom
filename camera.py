import pygame

from assets import Assets
from settings.constants import Constants
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

        self.half_w = self.width // 2
        self.half_h = self.height // 2

    def map_draw(self):
        from level import Level
        Level().screen.fill((0, 0, 0))
        player_offset_y = (SpriteGroups().player.rect.centery // self.quadrant_size)
        player_offset_x = (SpriteGroups().player.rect.centerx // self.quadrant_size)
        screen_limit_y = (Constants().screen_size[1] // self.quadrant_size)
        screen_limit_x = (Constants().screen_size[0] // self.quadrant_size)
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
        for i in range(1, len(self.map) - 1):
            for j in range(1, len(self.map[0]) - 1):
                div = self.map[i][j]
                cells_around = (self.map[i + 1][j], self.map[i - 1][j], self.map[i][j + 1], self.map[i][j - 1])
                diagonal_cells = (self.map[i + 1][j + 1], self.map[i - 1][j - 1],
                                  self.map[i - 1][j + 1], self.map[i + 1][j - 1])
                if div != Constants().EMPTY_CELL and Constants().EMPTY_CELL in cells_around:
                    Wall(
                        (self.quadrant_size * j + self.quadrant_size // 2,
                         self.quadrant_size * i + self.quadrant_size // 2),
                        SpriteGroups().walls_group)
                if div != Constants().EMPTY_CELL and Constants().ROAD_CELL.name in \
                        list(map(lambda cell: cell.name, cells_around)) and \
                        div.name != Constants().ROAD_CELL.name:
                    if len(list(filter(
                            lambda x: x.name == Constants().ROAD_CELL.name and x != Constants().EMPTY_CELL,
                            cells_around + diagonal_cells
                    ))) == 2:
                        Wall(
                            (self.quadrant_size * j + self.quadrant_size // 2,
                             self.quadrant_size * i + self.quadrant_size // 2),
                            SpriteGroups().walls_group)
                    else:
                        Door(
                            (self.quadrant_size * j + self.quadrant_size // 2,
                             self.quadrant_size * i + self.quadrant_size // 2),
                            SpriteGroups().doors_group)

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def draw_sprites(self, sprite_for_camera):
        self.center_target_camera(sprite_for_camera)
        self.map_draw()
        for sprite in sorted(
                self.sprites() +
                SpriteGroups().walls_group.sprites() +
                SpriteGroups().doors_group.sprites() +
                SpriteGroups().portal_group.sprites() +
                SpriteGroups().chests_group.sprites() +
                SpriteGroups().enemies_group.sprites() +
                SpriteGroups().bullets_group.sprites(),
                key=lambda x: x.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
