import random

import pygame

from assets import Assets
from sprites.inventory import InventoryV2
from sprites.sprite_groups import SpriteGroups
from sprites.weapons_list import WeaponsList


class DroppedWeapon(pygame.sprite.Sprite):
    def __init__(self, pos, group, item):
        super().__init__(group)
        self.image = Assets().images[item.image_name]
        self.rect = self.image.get_rect(center=pos)
        self.item = item

    def update(self):
        keys = pygame.key.get_pressed()
        if pygame.sprite.spritecollideany(self, SpriteGroups().camera_group):
            if keys[pygame.K_RETURN]:
                print("a")
                InventoryV2().dropped = True
                DroppedWeapon(SpriteGroups().player.pos, SpriteGroups().dropped_group,
                              InventoryV2().inventory[InventoryV2().inventory_item])

                InventoryV2().add_item_in_inventory_id(self.item, WeaponsList().weapons_list.index(self.item))
                self.kill()
                return
