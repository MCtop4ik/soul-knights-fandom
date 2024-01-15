import asyncio
import sqlite3
from dataclasses import dataclass
from pprint import pprint
from random import randrange

import pygame.sprite

from assets import Assets
from patterns.creational_patterns.singleton import Singleton


@dataclass
class Weapon:
    id: int
    weapon_name: str
    fire_damage: int
    cut_off: int
    offset_time: int
    image_name: str
    offset_x: int
    offset_y: int


class Inventory(metaclass=Singleton):

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
        self.inventory = Inventory()
        print(pos)
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        keys = pygame.key.get_pressed()
        bound_keyboard_keys = [pygame.K_1, pygame.K_2, pygame.K_3]
        for keyboard_key in bound_keyboard_keys:
            if keys[keyboard_key]:
                self.inventory.position_in_inventory = bound_keyboard_keys.index(keyboard_key)
                pprint(self.inventory.position_in_inventory)


class WeaponsList(metaclass=Singleton):
    def __init__(self):
        self.weapons_list = []
        self.connection = Assets.load_base()
        self.cursor = self.connection.cursor()

    def load_weapons_from_db(self):
        return self.cursor.execute('SELECT * FROM weapons').fetchall()

    def add_weapons_to_list(self):
        all_weapons = self.load_weapons_from_db()
        for weapon in all_weapons:
            self.weapons_list.append(Weapon(*weapon[:]))


def main():
    WeaponsList().add_weapons_to_list()


if __name__ == '__main__':
    main()
    print(WeaponsList().weapons_list)