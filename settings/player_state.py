from math import inf

from patterns.creational_patterns.singleton import Singleton


class PlayerState(metaclass=Singleton):
    def __init__(self):
        self.health = 1000
        self.energy = inf
        self.money = 0
        self.max_health = 1000
        self.max_energy = inf
