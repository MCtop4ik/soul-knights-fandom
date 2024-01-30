from math import inf

from patterns.creational_patterns.singleton import Singleton


class PlayerState(metaclass=Singleton):
    def __init__(self):
        self.health = 100
        self.energy = 100
        self.money = 0
        self.max_health = 100
        self.max_energy = 100
