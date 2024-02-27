import os
import random

from assets import Assets
from patterns.creational_patterns.singleton import Singleton
from .enemy_dataclass import Enemy


class EnemyList(metaclass=Singleton):
    def __init__(self):
        self.__enemies_list = []
        self.connection = Assets.load_base()
        self.cursor = self.connection.cursor()

    def load_weapons_from_db(self):
        return self.cursor.execute('SELECT * FROM enemies').fetchall()

    def add_enemies_to_list(self):
        all_enemies = self.load_weapons_from_db()
        for enemy in all_enemies:
            self.__enemies_list.append(Enemy(*enemy[:]))

    def get_random_enemy(self):
        return self.__enemies_list[random.randint(0, len(self.__enemies_list) - 1)]

    def load_enemy_sprites(self):
        return EnemyList.__get_all_file_names_from_directory('assets/images_test/enemy_images')

    @staticmethod
    def __get_all_file_names_from_directory(directory_path):
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        return files

    @property
    def enemies_list(self):
        return self.__enemies_list
