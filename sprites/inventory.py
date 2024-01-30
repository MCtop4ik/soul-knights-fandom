import pygame

from patterns.creational_patterns.singleton import Singleton
from sprites.item_sprites.dropped_weapon import DroppedWeapon
from sprites.sprite_groups import SpriteGroups
from sprites.weapons_list import WeaponsList


class InventoryV2(metaclass=Singleton):

    def __init__(self):
        self.inventory = []
        self.max_amount_of_items = 3
        self.__position_in_inventory = 0
        self.needChange = False
        self.dropped = False
    def add_item_in_inventory_without_drop(self, item):
        if len(self.inventory) < self.max_amount_of_items:
            self.inventory.append(item)
            return

        self.inventory.append(item)
        self.needChange = True

    def add_item_in_inventory(self, item):
        if len(self.inventory) < self.max_amount_of_items:
            # self.inventory.append(item)
            #dropped_item = self.inventory[self.__position_in_inventory]
            DroppedWeapon(SpriteGroups().player.pos, SpriteGroups().dropped_group, self.inventory[self.__position_in_inventory])

            self.inventory[self.__position_in_inventory] = item
            #dropped_item.drop()
            self.dropped = True
            self.needChange = True
            return

    def add_item_in_inventory_id(self, item, id):
        dropped_item = self.inventory[id]
        self.inventory[id] = item
        dropped_item.drop()

        self.needChange = True
        return dropped_item

    @staticmethod
    def get_bound_keyboard_keys():
        return [pygame.K_1, pygame.K_2, pygame.K_3]

    @property
    def position_in_inventory(self):
        return self.__position_in_inventory

    @property
    def inventory_item(self):
        return self.inventory[self.__position_in_inventory]

    @position_in_inventory.setter
    def position_in_inventory(self, new_position):
        self.__position_in_inventory = new_position
