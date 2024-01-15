from assets import Assets
from patterns.creational_patterns.singleton import Singleton
from .weapon import Weapon


class WeaponsList(metaclass=Singleton):
    def __init__(self):
        self.__weapons_list = []
        self.connection = Assets.load_base()
        self.cursor = self.connection.cursor()

    def load_weapons_from_db(self):
        return self.cursor.execute('SELECT * FROM weapons').fetchall()

    def add_weapons_to_list(self):
        all_weapons = self.load_weapons_from_db()
        for weapon in all_weapons:
            self.__weapons_list.append(Weapon(*weapon[:]))
        print(self.__weapons_list)

    @property
    def weapons_list(self):
        print(self.__weapons_list)
        return self.__weapons_list
