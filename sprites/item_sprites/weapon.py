import pygame
from pygame import Vector2

from assets import Assets
from sprites.sprite_groups import SpriteGroups


class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = Assets().images['chest']
        self.rect = self.image.get_rect(center=pos)
        self.shift = Vector2(10, 10)

    def update(self):
        self.rect = SpriteGroups().player.rect.copy()
        self.rect.x += 30
        self.rect.y += 30
