from math import sqrt, inf, atan2, pi
from random import randint, uniform

import pygame
from assets import Assets
from sprites.item_sprites.bullet import Bullet
from sprites.sprite_groups import SpriteGroups
from sprites.weapons_list import WeaponsList


class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.angle = 0
        self.offset_y = 20
        self.offset_x = 20
        self.offset_time_ms = 10
        self.cut_off = pi / 12
        self.fire_damage = 20
        self.last_shoot_time = 0
        self.rect = None
        self.image = None
        self.pos = pos
        self.group = group
        self.currentWeaponInt = 1
        self.change_weapon()

    def init_weapon(self, selected_weapon):
        self.last_shoot_time = 0

        self.image = Assets().images[selected_weapon.image_name]
        self.rect = self.image.get_rect(center=self.pos)
        self.rect.x += selected_weapon.offset_x
        self.rect.y = selected_weapon.offset_y
        self.offset_time_ms = selected_weapon.offset_time
        self.offset_x = selected_weapon.offset_x
        self.offset_y = selected_weapon.offset_y
        self.cut_off = pi / selected_weapon.cut_off
        self.fire_damage = selected_weapon.fire_damage

    def update(self):
        keys = pygame.key.get_pressed()
        self.rect = SpriteGroups().player.rect.copy()
        self.rect.x += self.offset_x
        self.rect.y += self.offset_y
        if keys[pygame.K_SPACE] and pygame.time.get_ticks() - self.last_shoot_time > self.offset_time_ms:
            self.shoot()
            self.last_shoot_time = pygame.time.get_ticks()

        if keys[pygame.K_1]:
            if self.currentWeaponInt != 1:
                self.currentWeaponInt = 1
                print("a")
                self.change_weapon(1)
        elif keys[pygame.K_2]:
            if self.currentWeaponInt != 2:
                self.currentWeaponInt = 2
                print("b")
                self.change_weapon(2)

    def radians_to_angle(self):
        self.angle = self.angle / pi * 180

    def compute_angle_to_fire(self):
        min_distant_to_enemy = inf
        nearest_enemy = None
        for enemy in SpriteGroups().enemies_group.sprites():
            if enemy.check_if_in_right_field():
                d = sqrt((SpriteGroups().player.rect.x - enemy.rect.x) ** 2 +
                         (SpriteGroups().player.rect.y - enemy.rect.y) ** 2)
                if d < min_distant_to_enemy:
                    min_distant_to_enemy = d
                    nearest_enemy = enemy
        if nearest_enemy is None:
            self.angle = randint(0, 360)
            return
        self.angle = atan2(nearest_enemy.rect.y - SpriteGroups().player.rect.y,
                           nearest_enemy.rect.x - SpriteGroups().player.rect.x) + uniform(-self.cut_off, self.cut_off)

    def shoot(self):
        self.compute_angle_to_fire()
        self.radians_to_angle()
        Bullet(SpriteGroups().bullets_group, self.angle, self.offset_x, self.offset_y,
               (SpriteGroups().player.rect.x,
                SpriteGroups().player.rect.y), 'player', 'chest', self.fire_damage)

    def change_weapon(self, weapon_id=1):
        selected_weapon = list(filter(lambda weapon: weapon.id == weapon_id, WeaponsList().weapons_list))[0]
        self.init_weapon(selected_weapon)
