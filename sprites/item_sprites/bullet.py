import pygame

from assets import Assets
from sprites.sprite_groups import SpriteGroups


class Bullet(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = Assets().images['chest']
        self.rect = self.image.get_rect(center=(SpriteGroups().player.rect.x,
                                                SpriteGroups().player.rect.y))
        self.speed = 1

    def update(self):
        self.rect.x += self.speed

