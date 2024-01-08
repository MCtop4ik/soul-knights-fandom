from random import randrange

from assets import Assets
from map_generation.cell import Cell
from map_generation.map_generator import MapGenerator
from map_generation.room_factory import RoomFactory
from settings.constants import Constants


class CreateFieldMatrix:

    def __init__(self):
        self.__field = []
        self.big_cell_size = Constants().big_cell_size

    def __create_field(self, field):
        height, width = len(field) * self.big_cell_size, len(field[0]) * self.big_cell_size
        self.__field = [[Constants().EMPTY_CELL for _ in range(width)] for _ in range(height)]

    def __find_corner_square(self, room_square):
        center_x = center_y = self.big_cell_size // 2
        room_height, room_width = len(room_square), len(room_square[0])
        return center_x - room_width // 2, center_y - room_height // 2

    def __add_room_in_field(self, room, x_corner, y_corner, i, j):
        delta_x, delta_y = i * self.big_cell_size + y_corner, j * self.big_cell_size + x_corner
        for i in range(len(room)):
            for j in range(len(room[i])):
                self.__field[delta_x + i][delta_y + j] = room[i][j]

    def __add_road_in_field(self, x_corner, y_corner, x, y):
        for i in range(y):
            for j in range(x):
                self.__field[x_corner + j][y_corner + i] = Cell(
                    Assets().road_image_ids[randrange(len(Assets().road_image_ids))],
                    'Road'
                )

    def __create_road(self, start_x, start_y, end_x, end_y):
        start_x, end_x = min(start_x, end_x), max(start_x, end_x)
        start_y, end_y = min(start_y, end_y), max(start_y, end_y)
        if start_x == end_x:
            for i in range(end_y - start_y):
                self.__add_road_in_field(
                    start_x - 2,
                    start_y + i,
                    5, 1
                )
        if start_y == end_y:
            for i in range(end_x - start_x):
                self.__add_road_in_field(
                    start_x + i,
                    start_y - 2,
                    1, 5
                )

    def generate_field(self):
        map_generator = MapGenerator(
            RoomFactory(Constants().name).read_level()
        )
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
        return self.__field,\
            coordinates[0],\
            coordinates[-1], \
            list(map(lambda x: x[1], coordinates_treasure_rooms))

    @staticmethod
    def print_field(field):
        for row in field:
            print(*row)
