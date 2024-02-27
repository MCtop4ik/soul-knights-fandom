from patterns.creational_patterns.singleton import Singleton


class Statistics(metaclass=Singleton):
    def __init__(self):
        self.killed_enemies = 0

    def killed_enemy(self):
        self.killed_enemies += 1

    def clear(self):
        self.killed_enemies = 0
