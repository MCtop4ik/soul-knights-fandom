from math import sqrt, inf, atan2, pi, cos, sin, radians
from random import randint, uniform

import pygame
from assets import Assets
from settings.player_state import PlayerState
from sprites.inventory import InventoryV2
from sprites.item_sprites.bullet import Bullet
from sprites.sprite_groups import SpriteGroups
from sprites.weapons_list import WeaponsList


class Weapon(pygame.sprite.Sprite):
    def __init__(self, weapon_id, pos, group):
        super().__init__(group)

        self.bullet_id = None
        self.angle = 0
        self.offset_y = 20
        self.offset_x = 20
        self.offset_time_ms = 10
        self.cut_off = pi / 12
        self.fire_damage = 20
        self.last_shoot_time = 0
        self.image = None
        self.pos = pos
        self.group = group
        self.current_position = 0
        self.sound_fire = pygame.mixer.Sound('assets/music/oi_new.mp3')
        self.energy_use = 1
        self.selected_weapon = None
        self.change_weapon(weapon_id)
        self.rect = (0, 0)
        self.chest = None
        self.is_melee = False

        self.last_tick = 0
        self.player_name = PlayerState().character
        self.hit_angle = 180

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
        self.bullet_id = selected_weapon.bullet_id
        self.selected_weapon = selected_weapon

    def update(self):
        keys = pygame.key.get_pressed()

        self.rect = SpriteGroups().player.rect.copy()
        self.rect.x += self.offset_x
        self.rect.y += self.offset_y
        if pygame.time.get_ticks() - self.last_tick > 90:
            self.image = Assets().images[f'{self.selected_weapon.image_name}']
            self.image = pygame.transform.rotate(self.image, self.angle)
            if SpriteGroups().player.look_side == 'left':
                self.image = pygame.transform.flip(self.image, True, False)
                self.offset_x = 0
            else:
                self.offset_x = self.selected_weapon.offset_x
            self.last_tick = pygame.time.get_ticks()
            if self.hit_angle < 180:
                self.hit()

        if keys[pygame.K_SPACE] and pygame.time.get_ticks() - self.last_shoot_time > self.offset_time_ms:
            if self.is_melee:
                self.hit_angle = 0
                self.hit()
                print('222')
            if not self.is_melee:
                self.shoot()
            self.last_shoot_time = pygame.time.get_ticks()
        inventory_position = InventoryV2().position_in_inventory
        if inventory_position != self.current_position:
            self.change_weapon(InventoryV2().inventory_item.id)
            self.current_position = inventory_position

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
        if SpriteGroups().player.use_energy(self.energy_use):
            self.compute_angle_to_fire()
            self.radians_to_angle()
            if SpriteGroups().player.look_side == 'left' and (-90 <= self.angle % 360 <= 90 or self.angle >= 270):
                SpriteGroups().player.look_side = 'right'
            elif SpriteGroups().player.look_side == 'right' and not (
                    -90 <= self.angle % 360 <= 90 or self.angle >= 270):
                SpriteGroups().player.look_side = 'left'
            bullet = list(filter(lambda x: x.id == self.bullet_id, WeaponsList().bullet_list))[0]
            bullet.fire_damage = self.fire_damage

            # self.sound_fire.set_volume(0.15)
            self.sound_fire.set_volume(0)
            self.sound_fire.play()
            Bullet(SpriteGroups().bullets_group, bullet, self.angle,
                   (SpriteGroups().player.rect.x,
                    SpriteGroups().player.rect.y), 'player')

    def rotate_sword(self):
        w, h = self.image.get_size()
        box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(self.angle) for p in box]
        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

        origin = (self.image.get_rect().x + min_box[0], self.image.get_rect().y - max_box[1])
        print(origin)
        self.rect = origin
        rotated_image = pygame.transform.rotate(self.image, self.hit_angle)
        self.image = rotated_image

    def hit(self):
        self.rotate_sword()
        self.rect = self.image.get_rect()
        enemy = pygame.sprite.spritecollideany(self, SpriteGroups().enemies_group)
        if enemy:
            print(self.fire_damage)
            enemy.damage(self.fire_damage)
        self.hit_angle += 20
        pygame.draw.rect(self.image, (255, 0, 0), self.image.get_rect(), 2)
        print(self.hit_angle)

    def change_weapon(self, weapon_id=1):
        selected_weapon = list(filter(lambda weapon: weapon.id == weapon_id, WeaponsList().weapons_list))[0]
        self.init_weapon(selected_weapon)
