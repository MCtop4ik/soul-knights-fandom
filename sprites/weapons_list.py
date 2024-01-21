from assets import Assets
from patterns.creational_patterns.singleton import Singleton
from .bullet_dataclass import Bullet
from .weapon_dataclass import Weapon
import os


class WeaponsList(metaclass=Singleton):
    def __init__(self):
        self.__weapons_list = []
        self.__bullet_list = []
        self.connection = Assets.load_base()
        self.cursor = self.connection.cursor()

    def load_weapons_from_db(self):
        return self.cursor.execute('SELECT * FROM weapons').fetchall()

    def add_weapons_to_list(self):
        all_weapons = self.load_weapons_from_db()
        for weapon in all_weapons:
            self.__weapons_list.append(Weapon(*weapon[:]))

    def load_bullets_from_db(self):
        return self.cursor.execute('SELECT * FROM bullets').fetchall()

    def load_weapons_sprites(self):
        path_lists = list(
            map(lambda path: "weapons/" + path, self.__get_all_file_names_from_directory('assets/images_test/weapons')))
        path_dict = {}
        for weapon_path in path_lists:
            key = "weapon_" + weapon_path.split('/')[-1].split('.')[0]
            path_dict[key] = weapon_path
        return path_dict

    @staticmethod
    def __get_all_file_names_from_directory(directory_path):
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        return files

    def add_bullets_to_list(self):
        all_bullets = self.load_bullets_from_db()
        for bullet in all_bullets:
            self.__bullet_list.append(Bullet(*bullet[:]))

    @property
    def weapons_list(self):
        return self.__weapons_list

    @property
    def bullet_list(self):
        return self.__bullet_list
