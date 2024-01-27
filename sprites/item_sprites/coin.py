from math import copysign

import pygame

from assets import Assets
from sprites.sprite_groups import SpriteGroups


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, group, coin_type='copper'):
        super().__init__(group)
        self.image = Assets().images[coin_type + '_coin']
        self.rect = self.image.get_rect(center=pos)
        self.speed = 4
        self.coin_type = coin_type
        self.last_timeout = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.last_timeout > 12:
            x_player, y_player = SpriteGroups().player.get_player_coordinates()
            relative_x = x_player - self.rect.centerx
            relative_y = y_player - self.rect.centery
            self.rect.centerx += copysign(1, relative_x) * self.speed
            self.rect.centery += copysign(1, relative_y) * self.speed

    def get_amount(self):
        return {
            'copper': 1,
            'silver': 3,
            'gold': 5
        }[self.coin_type]
