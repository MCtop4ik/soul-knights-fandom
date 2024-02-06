from map_generation.cell import Cell
from patterns.creational_patterns.singleton import Singleton


class Constants(metaclass=Singleton):

    def __init__(self):
        # size of one block image
        self.quadrant_size = 60
        # square root of amount of small squares in area of room
        self.big_cell_size = 50
        # player_size
        self.player_size = (60, 53)
        # player speed
        self.speed = 10
        # camera size
        self.camera_size = (1000, 800)
        # screen size
        self.screen_size = (1000, 800)
        # level which will load
        self.name = '2'
        self.FPS = 100
        self.music = 'Confrontation.mp3'

        # generation params
        self.min_enemies_rooms = 1
        self.max_enemies_rooms = 2
        self.max_treasuries_rooms = 3

        # treasury room spawn chance
        self.chance = 3
        self.iters_for_chance = 3

        self.fire_radius = self.quadrant_size * 10
        self.max_enemy_amount = 10
        self.min_enemy_amount = 3

        self.EMPTY_CELL = Cell(asset_abbr=0, name='Empty')
        self.ROAD_CELL = Cell(asset_abbr=2, name='Road')
