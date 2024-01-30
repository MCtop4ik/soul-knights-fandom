from math import inf

from patterns.creational_patterns.singleton import Singleton


class PlayerState(metaclass=Singleton):
    def __init__(self):
        self.health = 100
        self.energy = inf
        self.money = 0
