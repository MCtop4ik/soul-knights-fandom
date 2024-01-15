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


