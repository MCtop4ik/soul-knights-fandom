from math import inf

from patterns.creational_patterns.singleton import Singleton


class PlayerState(metaclass=Singleton):
    def __init__(self):
        self.health = 10000
        self.energy = inf
        self.money = 0
        self.max_health = 10000
        self.max_energy = inf
