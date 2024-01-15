from random import randrange

import pygame

from assets import Assets
from sprites.inventory import InventoryV2


class InventorySpriteV2(pygame.sprite.Sprite):

    def __init__(self, pos, group):
        super().__init__(group)

        self.image = Assets().images[
            Assets().wall_image_ids[
                randrange(len(Assets().wall_image_ids))
            ]
        ]
        self.inventory = InventoryV2()
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        keys = pygame.key.get_pressed()
        bound_keyboard_keys = self.inventory.get_bound_keyboard_keys()
        for keyboard_key in bound_keyboard_keys:
            if keys[keyboard_key]:
                self.inventory.position_in_inventory = bound_keyboard_keys.index(keyboard_key)
