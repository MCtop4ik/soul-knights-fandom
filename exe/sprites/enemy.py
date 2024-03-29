import random
from math import sqrt, atan2, pi, copysign

import pygame

from assets import Assets
from settings.constants import Constants
from settings.statistics import Statistics
from sprites.item_sprites.bullet import Bullet
from sprites.sprite_groups import SpriteGroups
from sprites.weapons_list import WeaponsList


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy, pos, room_coordinates, group):
        super().__init__(group)
        self.heal_points = enemy.heal_points
        self.cut_off = pi / enemy.cut_off
        self.offset_moved_time_ms = enemy.offset_moved_time
        self.offset_shoot_time_ms = enemy.offset_shoot_time
        self.speed = enemy.speed
        self.fire_radius_coefficient = enemy.fire_radius_coefficient
        self.image = Assets().images[enemy.asset_id]
        self.rect = self.image.get_rect(center=pos)
        self.pos = pos
        self.direction = pygame.math.Vector2()
        self.angle = 0
        self.last_shoot_time = 0
        self.last_moved_time = 0
        self.visible = False
        self.is_frozen = True
        self.room_coordinates = room_coordinates
        self.quadrant_size = Constants().quadrant_size
        self.big_cell_size = Constants().big_cell_size
        self.fire_radius = Constants().quadrant_size * self.fire_radius_coefficient

    def get_direction(self):
        x_player, y_player = SpriteGroups().player.get_player_coordinates()

        relative_x = x_player - self.rect.centerx
        relative_y = y_player - self.rect.centery

        self.angle = atan2(relative_y, relative_x) + random.uniform(-self.cut_off, self.cut_off)
        self.direction.x = copysign(1, relative_x)
        self.direction.y = copysign(1, relative_y)
        rnd_state = random.randint(1, 10)
        if 1 <= rnd_state <= 4:
            self.direction.x = copysign(1, relative_x)
        if 5 <= rnd_state <= 8:
            if copysign(1, relative_x) == 1:
                self.direction.x = 0
            if copysign(1, relative_x) == -1:
                self.direction.x = 0
            if copysign(1, relative_x) == 0:
                self.direction.x = [-1, 1][random.randint(0, 1)]
        if 9 <= rnd_state <= 10:
            if copysign(1, relative_x) == 0:
                self.direction.x = 0
            if copysign(1, relative_x) == -1:
                self.direction.x = 1
            if copysign(1, relative_x) == 1:
                self.direction.x = -1

    def to_radians(self):
        return self.angle * 180 / pi

    def fire(self):
        x_player, y_player = SpriteGroups().player.get_player_coordinates()
        if ((pygame.time.get_ticks() - self.last_shoot_time > self.offset_shoot_time_ms * random.randint(1, 10))
                and sqrt((x_player - self.rect.centerx) ** 2 + (
                        y_player - self.rect.centery) ** 2) < self.fire_radius * sqrt(2)):
            bullet = WeaponsList().bullet_list[1]
            bullet.fire_damage = 40
            Bullet(SpriteGroups().bullets_group, bullet, self.to_radians(), self.pos, 'enemy')
            self.last_shoot_time = pygame.time.get_ticks()

    def check_if_battle(self):
        self.is_frozen = not SpriteGroups().player.battle & SpriteGroups().player.not_allowed_through_doors

    def get_room(self):
        return self.room_coordinates

    def damage(self, damage):
        self.heal_points -= damage

    def check_if_in_right_field(self):
        x_player, y_player = (SpriteGroups().player.rect.centerx // (self.big_cell_size *
                                                                     self.quadrant_size),
                              SpriteGroups().player.rect.centery // (self.big_cell_size *
                                                                     self.quadrant_size))
        x_enemy, y_enemy = (self.rect.centerx // (self.big_cell_size * self.quadrant_size),
                            self.rect.centery // (self.big_cell_size * self.quadrant_size))
        return x_player == x_enemy and y_player == y_enemy

    def update(self):
        if self.heal_points <= 0:
            SpriteGroups().player.decrease_enemies_cnt(self.room_coordinates)
            Statistics().killed_enemy()
            self.kill()
        self.check_if_battle()
        if not self.is_frozen and self.check_if_in_right_field():
            self.get_direction()
            self.fire()
            if pygame.time.get_ticks() - self.last_moved_time > self.offset_moved_time_ms * random.randint(1, 10):
                self.rect.center += self.direction * self.speed
                self.last_moved_time = pygame.time.get_ticks()

            while (pygame.sprite.spritecollideany(self, SpriteGroups().walls_group) or
                   pygame.sprite.spritecollideany(self, SpriteGroups().doors_group) or
                    pygame.sprite.spritecollideany(self, SpriteGroups().boxes_group)):
                self.rect.center -= self.direction
