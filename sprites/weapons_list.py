from assets import Assets
from patterns.creational_patterns.singleton import Singleton
from .bullet_dataclass import Bullet
from .weapon_dataclass import Weapon


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

    def add_bullets_to_list(self):
        all_bullets = self.load_bullets_from_db()
        for bullet in all_bullets:
            print(Bullet(*bullet[:]))
            self.__bullet_list.append(Bullet(*bullet[:]))

    @property
    def weapons_list(self):
        return self.__weapons_list

    @property
    def bullet_list(self):
        return self.__bullet_list
