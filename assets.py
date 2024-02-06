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
            'energy': ('energy_stone.webp', (16, 16)),
            'copper_coin': ('coin.png', (16, 16)),
            'silver_coin': ('coin.png', (16, 16)),
            'gold_coin': ('coin.png', (16, 16)),
            'portal_0': ('transfer_gate_0.png', (self.quadrant_size * 2, self.quadrant_size * 3)),
            'portal_1': ('transfer_gate_1.png', (self.quadrant_size * 2, self.quadrant_size * 3)),
            'portal_2': ('transfer_gate_2.png', (self.quadrant_size * 2, self.quadrant_size * 3)),
            'portal_3': ('transfer_gate_3.png', (self.quadrant_size * 2, self.quadrant_size * 3)),
            'portal_4': ('transfer_gate_4.png', (self.quadrant_size * 2, self.quadrant_size * 3)),
            'portal_5': ('transfer_gate_5.png', (self.quadrant_size * 2, self.quadrant_size * 3)),
            'portal_6': ('transfer_gate_6.png', (self.quadrant_size * 2, self.quadrant_size * 3)),
            'portal_7': ('transfer_gate_7.png', (self.quadrant_size * 2, self.quadrant_size * 3))
        }
        # self.load_abbr({})

        self.__images = self.load_all_images()
        self.road_image_ids = RoomFactory(Constants().name).get_road_images()
        self.wall_image_ids = RoomFactory(Constants().name).get_wall_images()
        self.connection = self.load_base()
        self.connection.close()

    def load_player(self, player_name):
        print(player_name)
        abbr = {}
        for elem in self.__get_all_file_names_from_directory('assets/images_test/characters'):
            if elem[:len(player_name)] == player_name:
                abbr[elem.split('.')[0]] = self.load_image('characters/' + elem)
        print(abbr)
        self.__images = {**self.__images, **abbr}

    @staticmethod
    def __get_all_file_names_from_directory(directory_path):
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        return files

    def load_abbr(self, new_abbr):
        from sprites.weapons_list import WeaponsList
        self.abbr = {**new_abbr, **WeaponsList().load_weapons_sprites(), **WeaponsList().load_bullet_sprites()}
        self.__images = self.load_all_images()
        print(self.__images)

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
