import pygame

from assets import Assets
from sprites.sprite_groups import SpriteGroups


class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = Assets().images['chest']
        self.rect = self.image.get_rect(center=pos)



