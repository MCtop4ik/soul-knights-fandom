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
            'door': 'player.png',
            'portal': 'player.png',
            'chest': 'player-alpha-2.png',
            'enemy1': 'player-alpha.png',
            'enemy2': 'player.png'
        }
        self.__images = self.load_all_images()
        self.road_image_ids = RoomFactory(Constants().name).get_road_images()
        self.wall_image_ids = RoomFactory(Constants().name).get_wall_images()
        self.connection = self.load_base()
        self.connection.close()

    def load_abbr(self, new_abbr):
        self.abbr = new_abbr
        self.__images = self.load_all_images()

    def load_image(self, name):
        fullname = os.path.join('assets/images_test', name)
        if not os.path.isfile(fullname):
            return
        image = pygame.transform.scale(pygame.image.load(fullname), (self.quadrant_size, self.quadrant_size))
        return image

    def load_all_images(self):
        images = {}
        for key, value in {**self.constant_images, **self.abbr}.items():
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
