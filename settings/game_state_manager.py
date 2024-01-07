from patterns.creational_patterns.singleton import Singleton


class GameStateManager(metaclass=Singleton):

    def __init__(self):
        self.next_level = False
