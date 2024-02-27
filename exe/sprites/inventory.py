import pygame

from patterns.creational_patterns.singleton import Singleton


class InventoryV2(metaclass=Singleton):

    def __init__(self):
        self.inventory = []
        self.max_amount_of_items = 3
        self.__position_in_inventory = 0

    def add_item_in_inventory(self, item):
        if len(self.inventory) < self.max_amount_of_items:
            self.inventory = (self.inventory[:self.__position_in_inventory] + [item] +
                              self.inventory[self.__position_in_inventory:])
            return
        dropped_item = self.inventory.pop(self.__position_in_inventory)
        self.inventory = (self.inventory[:self.__position_in_inventory] + [item] +
                          self.inventory[self.__position_in_inventory:])
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


if __name__ == "__main__":
    inventory = InventoryV2()
    inventory.add_item_in_inventory('test1')
    inventory.add_item_in_inventory('test2')
    inventory.add_item_in_inventory('test3')
    print(inventory.inventory)
    inventory.add_item_in_inventory('test2')
    print(inventory.inventory)
    inventory.add_item_in_inventory('test1')
    inventory.add_item_in_inventory('test2')
    inventory.add_item_in_inventory('test1')
    print(inventory.inventory)


