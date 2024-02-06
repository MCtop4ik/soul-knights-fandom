from math import inf

from patterns.creational_patterns.singleton import Singleton


class PlayerState(metaclass=Singleton):
    def __init__(self):
        self.health = 500
        self.energy = 300
        self.money = 0
        self.max_health = 500
        self.max_energy = 300
