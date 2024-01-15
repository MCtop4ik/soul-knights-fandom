from dataclasses import dataclass
from random import randrange

import pygame.sprite

from assets import Assets
from patterns.creational_patterns.singleton import Singleton


@dataclass
class ItemProp:
    name: str
    type: int


@dataclass
class Weapon:
    name: str
    type: int
    asset_id: int
    damage: int
    accessory: int
    mana: int
    activation_speed: int
    fire_speed: int
    price: int


@dataclass
class Armor:
    name: str
    type: int
    asset_id: int
    safe: int
    accessory: None
    price: int


@dataclass
class HealProps(ItemProp):
    asset_id: int
    heal: int


@dataclass
class MagicProps(ItemProp):
    asset_id: int
    mane: int
    price: int


class Inventory(metaclass=Singleton):
    def __init__(self):
        self.inventory = []
        self.max_prop = 5

    def add_in_inventory(self, prop):
        if len(self.inventory) < self.max_prop:
            self.inventory.append(prop)
            return None
        drop_prop = self.inventory.pop()
        self.inventory.append(prop)
        return drop_prop


class InventoryArmorSprite(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = Assets().images[
            Assets().wall_image_ids[
                randrange(len(Assets().wall_image_ids))
            ]
        ]
        self.rect = self.image.get_rect(center=pos)


class InventoryPocketSprite(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = Assets().images[
            Assets().wall_image_ids[
                randrange(len(Assets().wall_image_ids))
            ]
        ]
        self.rect = self.image.get_rect(center=pos)
