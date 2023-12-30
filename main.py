import os
import sys
from dataclasses import dataclass
from random import randint, randrange
from typing import List

import pygame


@dataclass
class Cell:
    asset_abbr: int
    name: str


@dataclass(frozen=True)
class Room:
    matrix: List[List[Cell]]


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Assets(metaclass=Singleton):

    def __init__(self, quadrant_size):
        self.quadrant_size = quadrant_size
        self.abbr = {
            1: '1.jpg',
            2: 'player-alpha-2.png',
            3: '3.png',
            4: 'wall.png'
        }
        self.__images = self.load_all_images()
        self.__player = self.load_image('player.png')

    def load_image(self, name):
        fullname = os.path.join('assets', name)
        if not os.path.isfile(fullname):
            return
        image = pygame.transform.scale(pygame.image.load(fullname), (self.quadrant_size, self.quadrant_size))
        return image

    def load_all_images(self):
        images = {}
        for key, value in self.abbr.items():
            images[key] = self.load_image(value)
        return images

    def get_player(self):
        return self.__player

    @property
    def images(self):
        return self.__images


class MapGenerator:

    def __init__(self):
        self.start_room = Room([[Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start')],
                                [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start')],
                                [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start')],
                                [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start')],
                                [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start')],
                                [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start')],
                                [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start')],
                                [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start')],
                                [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start')],
                                [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start')],
                                [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start')],
                                [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start')],
                                [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start')],
                                [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                 Cell(1, 'Start'), Cell(1, 'Start')]
                                ])
        self.portal_room = Room([[Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start')],
                                 [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start')],
                                 [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start')],
                                 [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start')],
                                 [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start')],
                                 [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start')],
                                 [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start')],
                                 [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start')],
                                 [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start')],
                                 [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start')],
                                 [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start')],
                                 [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start')],
                                 [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start')],
                                 [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                  Cell(1, 'Start'), Cell(1, 'Start')]
                                 ])
        self.enemy_rooms = [Room([[Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')]
                                  ]),
                            Room([[Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')],
                                  [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                   Cell(1, 'Start'), Cell(1, 'Start')]
                                  ])]
        self.treasure_rooms = [Room([[Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')]
                                     ]),
                               Room([[Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')],
                                     [Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'), Cell(1, 'Start'),
                                      Cell(1, 'Start'), Cell(1, 'Start')]
                                     ])]
        self.rooms_amount = 10
        self.__min_enemies_rooms = 2
        self.__max_enemies_rooms = 5
        self.__max_treasuries_rooms = 3
        self.__rooms = self.__create_rooms_matrix()
        self.__all_coordinates = []
        self.__coordinates = [(self.rooms_amount + 1, self.rooms_amount + 1)]
        self.__coordinates_for_treasure_room = []

    def __create_rooms_matrix(self):
        rooms = [[None for _ in range(self.rooms_amount * 2 + 1)] for _ in range(self.rooms_amount * 2 + 1)]
        rooms[self.rooms_amount + 1][self.rooms_amount + 1] = self.start_room
        return rooms

    def __create_room(self, amount, rooms):
        x_gen, y_gen = self.__coordinates[-1]
        for _ in range(amount):
            alias_move = [-1, 1][randint(0, 1)]
            direction = ['X', 'Y'][randint(0, 1)]
            while self.__rooms[
                x_gen + alias_move if direction == 'X' else x_gen
            ][y_gen + alias_move if direction == 'Y' else y_gen] is not None:
                alias_move = [-1, 1][randint(0, 1)]
                direction = ['X', 'Y'][randint(0, 1)]
            if direction == 'X':
                x_gen += alias_move
            if direction == 'Y':
                y_gen += alias_move
            self.__coordinates.append((x_gen, y_gen))
            self.__rooms[x_gen][y_gen] = rooms[randrange(len(rooms))]

    def __create_enemy_rooms(self):
        enemies_rooms_number = randint(self.__min_enemies_rooms, self.__max_enemies_rooms)
        self.__create_room(enemies_rooms_number, self.enemy_rooms)

    def __create_portal_room(self):
        self.__create_room(1, [self.portal_room])

    def __create_treasure_rooms(self):
        cnt_treasuries = 0
        left_shift = 1
        right_shift = 1
        chance = 3
        iters_for_chance = 3

        for enemy_room_coordinate in self.__coordinates[left_shift:-right_shift]:
            x_enemy_room, y_enemy_room = enemy_room_coordinate
            for _ in range(iters_for_chance):
                if cnt_treasuries >= self.__max_treasuries_rooms:
                    return
                alias_move = [-1, 1][randint(0, 1)]
                direction = ['X', 'Y'][randint(0, 1)]
                if self.__rooms[
                    x_enemy_room + alias_move if direction == 'X' else x_enemy_room
                ][y_enemy_room + alias_move if direction == 'Y' else y_enemy_room] is None:
                    if randint(0, chance) == randint(0, chance):
                        coordinate_enemy_for_treasure_room = [(x_enemy_room, y_enemy_room)]
                        if direction == 'X':
                            x_enemy_room += alias_move
                        if direction == 'Y':
                            y_enemy_room += alias_move
                        coordinate_enemy_for_treasure_room.append((x_enemy_room, y_enemy_room))
                        self.__coordinates_for_treasure_room.append(coordinate_enemy_for_treasure_room)
                        self.__all_coordinates.append((x_enemy_room, y_enemy_room))
                        self.__rooms[x_enemy_room][y_enemy_room] = self.treasure_rooms[
                            randrange(len(self.treasure_rooms))
                        ]
                        cnt_treasuries += 1

    def __crop(self):
        new_rooms = list()
        for i in range(len(self.__rooms)):
            if any(elem is not None for elem in self.__rooms[i]):
                new_rooms.append(self.__rooms[i])
        self.__rooms = new_rooms
        new_rooms = list()
        rooms_transposed = tuple(zip(*self.__rooms[::-1]))
        for i in range(len(rooms_transposed)):
            if any(elem is not None for elem in rooms_transposed[i]):
                new_rooms.append(rooms_transposed[i])
        for _ in range(3):
            new_rooms = list(zip(*new_rooms[::-1]))
        self.__rooms = new_rooms
        min_x = min(self.__all_coordinates, key=lambda elem: elem[0])[0]
        min_y = min(self.__all_coordinates, key=lambda elem: elem[1])[1]
        self.__coordinates = list(map(
            lambda coordinate: (coordinate[0] - min_x, coordinate[1] - min_y), self.__coordinates))
        self.__coordinates_for_treasure_room = list(map(
            lambda coordinate: [(coordinate[0][0] - min_x, coordinate[0][1] - min_y), (
                coordinate[1][0] - min_x, coordinate[1][1] - min_y)], self.__coordinates_for_treasure_room))

    def generate(self):
        self.__create_enemy_rooms()
        self.__create_portal_room()
        self.__create_treasure_rooms()
        self.__all_coordinates += self.__coordinates
        self.__crop()
        return self.__rooms, self.__coordinates, self.__coordinates_for_treasure_room


class CreateFieldMatrix:

    def __init__(self):
        self.__field = []
        self.big_cell_size = 50

    def __create_field(self, field):
        height, width = len(field) * self.big_cell_size, len(field[0]) * self.big_cell_size
        self.__field = [[0 for _ in range(width)] for _ in range(height)]

    def __find_corner_square(self, room_square):
        center_x = center_y = self.big_cell_size // 2
        room_height, room_width = len(room_square), len(room_square[0])
        return center_x - room_width // 2, center_y - room_height // 2

    def __add_room_in_field(self, room, x_corner, y_corner, i, j):
        delta_x, delta_y = i * self.big_cell_size + y_corner, j * self.big_cell_size + x_corner
        for i in range(len(room)):
            for j in range(len(room[i])):
                self.__field[delta_x + i][delta_y + j] = room[i][j]

    def __create_road(self, start_x, start_y, end_x, end_y):
        start_x, end_x = min(start_x, end_x), max(start_x, end_x)
        start_y, end_y = min(start_y, end_y), max(start_y, end_y)
        if start_x == end_x:
            for i in range(end_y - start_y):
                self.__field[start_x][start_y + i] = Cell(2, 'road')
                self.__field[start_x + 1][start_y + i] = Cell(2, 'road')
                self.__field[start_x - 1][start_y + i] = Cell(2, 'road')
                self.__field[start_x + 2][start_y + i] = Cell(2, 'road')
                self.__field[start_x - 2][start_y + i] = Cell(2, 'road')
        if start_y == end_y:
            for i in range(end_x - start_x):
                self.__field[start_x + i][start_y] = Cell(2, 'road')
                self.__field[start_x + i][start_y + 1] = Cell(2, 'road')
                self.__field[start_x + i][start_y - 1] = Cell(2, 'road')
                self.__field[start_x + i][start_y + 2] = Cell(2, 'road')
                self.__field[start_x + i][start_y - 2] = Cell(2, 'road')

    def generate_field(self):
        map_generator = MapGenerator()
        field, coordinates, coordinates_treasure_rooms = map_generator.generate()
        self.__create_field(field)
        for i in range(1, len(coordinates)):
            self.__create_road(
                start_x=coordinates[i - 1][0] * self.big_cell_size + self.big_cell_size // 2,
                start_y=coordinates[i - 1][1] * self.big_cell_size + self.big_cell_size // 2,
                end_x=coordinates[i][0] * self.big_cell_size + self.big_cell_size // 2,
                end_y=coordinates[i][1] * self.big_cell_size + self.big_cell_size // 2
            )
        print(coordinates_treasure_rooms)
        for i in range(len(coordinates_treasure_rooms)):
            self.__create_road(
                start_x=coordinates_treasure_rooms[i][0][0] * self.big_cell_size + self.big_cell_size // 2,
                start_y=coordinates_treasure_rooms[i][0][1] * self.big_cell_size + self.big_cell_size // 2,
                end_x=coordinates_treasure_rooms[i][1][0] * self.big_cell_size + self.big_cell_size // 2,
                end_y=coordinates_treasure_rooms[i][1][1] * self.big_cell_size + self.big_cell_size // 2
            )
        for i in range(len(field)):
            for j in range(len(field[i])):
                field_square = field[i][j]
                if field_square is not None:
                    room = field_square.matrix
                    x_corner, y_corner = self.__find_corner_square(room)
                    self.__add_room_in_field(room, x_corner, y_corner, i, j)
        self.print_field(field)
        return self.__field, coordinates[0]

    def print_field(self, field):
        for row in field:
            print(*row)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, player_size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load('assets/player.png').convert_alpha(), player_size)
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 10

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self):
        self.input()
        self.rect.center += self.direction * self.speed
        if pygame.sprite.spritecollideany(self, wall_group):
            self.rect.center -= self.direction * self.speed


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, quadrant_size, group):
        super().__init__(group)
        self.image = Assets(quadrant_size).images[4]
        self.rect = self.image.get_rect(center=pos)


class CameraGroup(pygame.sprite.Group):
    EMPTY_CELL = 0

    def __init__(self, width, height, quadrant_size, lvl):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.quadrant_size = quadrant_size
        self.width, self.height = width, height

        self.map = lvl
        self.assets = Assets(self.quadrant_size)

        self.offset = pygame.math.Vector2()

        self.half_w = self.width // 2
        self.half_h = self.height // 2

    def map_draw(self):
        screen.fill((0, 0, 0))
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                div = self.map[i][j]
                if div != self.EMPTY_CELL:
                    ground_surf = self.assets.images[div.asset_abbr]
                    self.display_surface.blit(
                        ground_surf,
                        (self.quadrant_size * j, self.quadrant_size * i) - self.offset)

    def wall_draw(self):
        for i in range(1, len(self.map) - 1):
            for j in range(1, len(self.map[0]) - 1):
                div = self.map[i][j]
                if div != self.EMPTY_CELL and self.EMPTY_CELL in (
                        self.map[i + 1][j], self.map[i - 1][j],
                        self.map[i][j + 1], self.map[i][j - 1]):
                    Wall(
                        (self.quadrant_size * j + self.quadrant_size // 2,
                         self.quadrant_size * i + self.quadrant_size // 2),
                        self.quadrant_size, wall_group)

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def draw_sprites(self, sprite_for_camera):
        self.center_target_camera(sprite_for_camera)
        self.map_draw()
        for sprite in sorted(self.sprites() + wall_group.sprites(), key=lambda x: x.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)


clock = pygame.time.Clock()
q_s = 40
b_c_s = 50
screen = pygame.display.set_mode((800, 800))
level, start_coordinates = CreateFieldMatrix().generate_field()
camera_group = CameraGroup(600, 600, q_s, level)
player = Player(
    (start_coordinates[0] * q_s * b_c_s + (q_s * b_c_s) // 2, start_coordinates[1] * q_s * b_c_s + (q_s * b_c_s) // 2),
    (40, 40),
    camera_group)
wall_group = pygame.sprite.Group()
camera_group.wall_draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    camera_group.update()
    camera_group.draw_sprites(player)

    pygame.display.update()
    clock.tick(60)
