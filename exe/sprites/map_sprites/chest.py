import random

import pygame

from assets import Assets
from sprites.inventory import InventoryV2
from sprites.item_sprites.dropped_weapon import DroppedWeapon
from sprites.sprite_groups import SpriteGroups
from sprites.weapons_list import WeaponsList


class Chest(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = Assets().images['chest']
        self.rect = self.image.get_rect(center=pos)
        self.opened = False

    def update(self):
        keys = pygame.key.get_pressed()
        if pygame.sprite.spritecollideany(self, SpriteGroups().camera_group) and not self.opened:
            if keys[pygame.K_RETURN]:
                self.opened = True
                DroppedWeapon(WeaponsList().random_weapon(),
                              self.rect.center, SpriteGroups().dropped_items_group)
