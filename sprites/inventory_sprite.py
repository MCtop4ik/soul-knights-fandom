from random import randrange

import pygame

from assets import Assets
from sprites.inventory import InventoryV2


class InventorySpriteV2(pygame.sprite.Sprite):

    def __init__(self, pos, group):
        super().__init__(group)
        self.inventory = InventoryV2()
        self.image = Assets().images[self.inventory.inventory_item.image_name]
        self.rect = self.image.get_rect(center=pos)
        self.lastKey = 1

    def update(self):

        keys = pygame.key.get_pressed()
        bound_keyboard_keys = self.inventory.get_bound_keyboard_keys()
        for keyboard_key in bound_keyboard_keys:
            if keys[keyboard_key]:
                self.inventory.position_in_inventory = bound_keyboard_keys.index(keyboard_key)
                self.lastKey = keyboard_key
                if self.inventory.position_in_inventory < len(Assets().images):
                    self.image = Assets().images[self.inventory.inventory_item.image_name]
        if self.image != Assets().images[self.inventory.inventory_item.image_name]:
            self.inventory.position_in_inventory = bound_keyboard_keys.index(self.lastKey)

            self.image = Assets().images[self.inventory.inventory_item.image_name]
