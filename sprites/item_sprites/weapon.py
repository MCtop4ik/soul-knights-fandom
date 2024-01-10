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

    def update(self):
        keys = pygame.key.get_pressed()
        self.rect = SpriteGroups().player.rect.copy()
        self.rect.x += 30
        self.rect.y += 30

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        Bullet(SpriteGroups().bullets_group)
