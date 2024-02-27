import pygame
from pygame.sprite import Group

from patterns.creational_patterns.singleton import Singleton


class SpriteGroups(metaclass=Singleton):

    def __init__(self):
        self.walls_group = Group()
        self.doors_group = Group()
        self.boxes_group = Group()
        self.portal_group = Group()
        self.chests_group = Group()
        self.camera_group = Group()
        self.enemies_group = Group()
        self.weapon_group = Group()
        self.bullets_group = Group()
        self.dropped_items_group = Group()
        self.inventory_group = Group()
        self.energy_group = Group()
        self.coins_group = Group()
        self.weapon = None
        self.player = None

    def clear_level_sprites(self):
        self.doors_group = pygame.sprite.Group()
        self.walls_group = pygame.sprite.Group()
        self.portal_group = pygame.sprite.Group()
        self.chests_group = pygame.sprite.Group()
        self.boxes_group = pygame.sprite.Group()
        self.energy_group = pygame.sprite.Group()
        self.enemies_group = pygame.sprite.Group()
        self.inventory_group = pygame.sprite.Group()
        self.energy_group = pygame.sprite.Group()
        self.dropped_items_group = pygame.sprite.Group()
        self.energy_group = Group()
        self.coins_group = Group()


if __name__ == "__main__":
    s = SpriteGroups()
    s.clear_level_sprites()
