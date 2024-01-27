import random

import pygame

from assets import Assets
from sprites.item_sprites.coin import Coin
from sprites.item_sprites.energy import Energy
from sprites.sprite_groups import SpriteGroups


class Box(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = Assets().images['box']
        self.rect = self.image.get_rect(center=pos)
        self.health = 100

    def damage(self, damage):
        self.health -= damage

    def update(self):
        if self.health <= 0:
            if random.randint(1, 100) in range(1, 5 + 1):
                Energy(self.rect.center, SpriteGroups().energy_group)
                print('energy')
            if random.randint(1, 100) == 1:
                Coin(self.rect.center, SpriteGroups().energy_group, coin_type='copper')
                print('coin')
            self.kill()
