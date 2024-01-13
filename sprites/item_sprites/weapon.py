import pygame
from pygame import Vector2

from assets import Assets
from sprites.item_sprites.bullet import Bullet
from sprites.sprite_groups import SpriteGroups


class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = Assets().images['chest']
        self.rect = self.image.get_rect(center=pos)
        self.shift = Vector2(10, 10)
        self.last_shoot_time = 0
        self.offset_time_ms = 100
        self.angle = 0

    def update(self):
        keys = pygame.key.get_pressed()
        self.rect = SpriteGroups().player.rect.copy()
        self.rect.x += 30
        self.rect.y += 30
        if keys[pygame.K_SPACE] and pygame.time.get_ticks() - self.last_shoot_time > self.offset_time_ms:
            self.shoot()
            self.last_shoot_time = pygame.time.get_ticks()

    def shoot(self):
        print(self.angle)
        Bullet(SpriteGroups().bullets_group, self.angle)
        self.angle = (self.angle + 10) % 360
