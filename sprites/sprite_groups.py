from pygame.sprite import Group

from patterns.creational_patterns.singleton import Singleton


class SpriteGroups(metaclass=Singleton):

    def __init__(self):
        self.walls_group = Group()
        self.doors_group = Group()
        self.portal_group = Group()
        self.camera_group = Group()
        self.player = None
