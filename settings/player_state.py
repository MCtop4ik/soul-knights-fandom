from patterns.creational_patterns.singleton import Singleton


class PlayerState(metaclass=Singleton):
    def __init__(self):
        self.character = 'vampire_13'

        self.health = 1000
        self.energy = 500
        self.money = 0
        self.max_health = 1000
        self.max_energy = 500
        self.levels = ['2']
        self.level_index = 0
