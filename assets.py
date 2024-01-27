import os
import sqlite3

import pygame
from patterns.creational_patterns.singleton import Singleton
from settings.constants import Constants


class Assets(metaclass=Singleton):

    def __init__(self):
        from map_generation.room_factory import RoomFactory
        self.quadrant_size = Constants().quadrant_size
        self.abbr = {}
        self.constant_images = {
            'door': 'player_.png',
            'portal': ('portal.png', (self.quadrant_size * 2, self.quadrant_size * 3)),
            'chest': 'chest.jpg',
            'enemy1': '0.jpeg',
            'enemy2': 'player.png',
            'enemy3': 'victor.png',
            'senya': 'bullet.png',
            'box': 'box_sprite.webp',
            'energy': ('energy_stone.webp', (16, 16))
        }
        # self.load_abbr({})

        self.__images = self.load_all_images()
        self.road_image_ids = RoomFactory(Constants().name).get_road_images()
        self.wall_image_ids = RoomFactory(Constants().name).get_wall_images()
        self.connection = self.load_base()
        self.connection.close()

    def load_abbr(self, new_abbr):
        from sprites.weapons_list import WeaponsList
        self.abbr = {**new_abbr, **WeaponsList().load_weapons_sprites()}
        self.__images = self.load_all_images()

    def load_image(self, name):
        fullname = os.path.join('assets/images_test', name)
        if not os.path.isfile(fullname):
            return
        image = pygame.transform.scale(pygame.image.load(fullname), (self.quadrant_size, self.quadrant_size))
        return image

    def load_image_with_size(self, name, size):
        fullname = os.path.join('assets/images_test', name)
        if not os.path.isfile(fullname):
            return
        image = pygame.transform.scale(pygame.image.load(fullname), size)
        return image

    def load_all_images(self):
        images = {}
        for key, value in {**self.constant_images, **self.abbr}.items():
            if type(value) is tuple:
                images[key] = self.load_image_with_size(value[0], value[1])
            else:
                images[key] = self.load_image(value)
        return images

    @property
    def images(self):
        return self.__images

    @staticmethod
    def load_base():
        fullname = os.path.join('assets/bases', "database.db")
        if not os.path.isfile(fullname):
            return
        connection = sqlite3.connect(fullname)
        return connection
