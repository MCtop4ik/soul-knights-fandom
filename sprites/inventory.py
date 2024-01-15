from pprint import pprint
from random import randrange

import pygame.sprite

from assets import Assets
from patterns.creational_patterns.singleton import Singleton


class InventoryV2(metaclass=Singleton):

    def __init__(self):
        self.inventory = []
        self.max_amount_of_items = 3
        self.__position_in_inventory = 0

    def add_item_in_inventory(self, item):
        if len(self.inventory) < self.max_amount_of_items:
            self.inventory.append(item)
            return
        dropped_item = self.inventory.pop(self.__position_in_inventory)
        self.inventory.append(item)
        return dropped_item

    @property
    def position_in_inventory(self):
        return self.__position_in_inventory

    @position_in_inventory.setter
    def position_in_inventory(self, new_position):
        self.__position_in_inventory = new_position


class InventorySpriteV2(pygame.sprite.Sprite):

    def __init__(self, pos, group):
        super().__init__(group)

        self.image = Assets().images[
            Assets().wall_image_ids[
                randrange(len(Assets().wall_image_ids))
            ]
        ]
        self.inventory = InventoryV2()
        print(pos)
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        keys = pygame.key.get_pressed()
        bound_keyboard_keys = [pygame.K_1, pygame.K_2, pygame.K_3]
        for keyboard_key in bound_keyboard_keys:
            if keys[keyboard_key]:
                self.inventory.position_in_inventory = bound_keyboard_keys.index(keyboard_key)
                pprint(self.inventory.position_in_inventory)
