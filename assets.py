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
            'enemy': 'player-alpha.png'
        }
        self.__images = self.load_all_images()
        self.__player = self.load_image('player.png')
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

    def get_player(self):
        return self.__player

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
