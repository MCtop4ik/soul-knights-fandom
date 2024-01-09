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
        self.MAX_ARMORS = 1
        self.MAX_INV = 10
        self.MAX_POCKET = 3
        self.MAX_HAND = 1
        self.inv = []
        self.hand = []
        self.pocket = []
        self.armors = []
        self.player: int = -1

    def add_prop_in_inv(self, prop):
        if len(self.inv) >= self.MAX_INV:
            drop_prop = self.inv.pop()
            self.inv.append(prop)
            return drop_prop
        else:
            self.inv.append(prop)

    def add_weapon_in_hand(self, other_weapon: Weapon) -> Weapon or None:
        if len(self.hand) >= self.MAX_HAND:
            drop_weapon = self.hand.pop()
            self.hand.append(other_weapon)
            self.add_prop_in_inv(drop_weapon)
        else:
            self.hand.append(other_weapon)

    def add_armor(self, other_armor: Armor) -> Armor or None:
        if len(self.armors) >= self.MAX_ARMORS:
            drop_armor = self.armors.pop()
            self.armors.append(other_armor)
            self.add_prop_in_inv(drop_armor)
        else:
            self.armors.append(other_armor)

    def add_inventory(self, prop):
        self.add_prop_in_inv(prop)

    def add_pocket(self, prop):
        if len(self.pocket) >= self.MAX_POCKET:
            self.add_prop_in_inv(prop)
        else:
            self.pocket.append(prop)


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
