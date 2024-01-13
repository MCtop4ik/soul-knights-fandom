import random
from math import sqrt, atan2, pi

import pygame

from assets import Assets
from settings.constants import Constants
from sprites.item_sprites.bullet import Bullet
from sprites.sprite_groups import SpriteGroups


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = Assets().images['enemy']
        self.rect = self.image.get_rect(center=pos)
        self.pos = pos
        self.direction = pygame.math.Vector2()
        self.speed = 15
        self.angle = 0
        self.offset_time_ms = 1000
        self.last_shoot_time = 0

    def get_direction(self):
        x_player, y_player = SpriteGroups().player.get_player_coordinates()

        relative_x = -(self.rect.centerx - x_player)
        relative_y = -(self.rect.centery - y_player)

        self.angle = atan2(relative_y, relative_x)

        # if sqrt(x_player ** 2 + y_player ** 2) - \
        #         sqrt(self.rect.centerx ** 2 + self.rect.centery ** 2) < Constants().fire_radius * sqrt(2):
        #     pass

        # if keys[pygame.K_UP] or keys[pygame.K_w]:
        #     self.direction.y = -1
        # elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        #     self.direction.y = 1
        # else:
        #     self.direction.y = 0
        #
        # if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        #     self.direction.x = 1
        # elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        #     self.direction.x = -1
        # else:
        #     self.direction.x = 0

    def to_radians(self):
        return self.angle * 180 / pi

    def fire(self):
        x_player, y_player = SpriteGroups().player.get_player_coordinates()
        if (pygame.time.get_ticks() - self.last_shoot_time > self.offset_time_ms * random.randint(1, 10)) and sqrt(
                (x_player - self.rect.centerx) ** 2 + (
                        y_player - self.rect.centery) ** 2) < Constants().fire_radius * sqrt(2):
            Bullet(SpriteGroups().bullets_group, self.to_radians(), 50, 60, self.pos, 'chest')
            self.last_shoot_time = pygame.time.get_ticks()

    def update(self):
        self.get_direction()
        self.fire()
        self.rect.center += self.direction * self.speed

        while pygame.sprite.spritecollideany(self, SpriteGroups().walls_group):
            self.rect.center -= self.direction
