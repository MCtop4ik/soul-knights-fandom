import os
from dataclasses import dataclass
from random import randint, randrange
from typing import List

import pygame


@dataclass
class Cell:
    color: tuple
    asset_link: str
    is_empty: bool


@dataclass(frozen=True)
class Room:
    matrix: List[List[Cell]]


class Wall(Cell):
    pass


class MapGenerator:

    def __init__(self):
        self.start_room = Room([[Cell((100, 255, 255), 'Start', True), Cell((100, 255, 255), 'Start ', True)],
                                [Cell((100, 255, 255), 'Start ', True), Cell((100, 255, 255), 'Start ', True)],
                                [Cell((100, 255, 255), 'Start ', True), Cell((100, 100, 255), 'Start ', True)],
                                [Cell((100, 255, 255), 'Start ', True), Cell((100, 255, 255), 'Start ', True)],
                                [Cell((100, 255, 255), 'Start ', True), Cell((100, 255, 255), 'Start ', True)]])
        # self.portal_room = Room([[Cell('Portal', True), Cell('Portal', True)],
        #                          [Cell('Portal', True), Cell('Portal', True)]])
        # self.enemy_room = Room([[Cell('Enemy ', True), Cell('Enemy ', True)],
        #                         [Cell('Enemy ', True), Cell('Enemy ', True)]])
        # self.treasure_room = Room([[Cell('Treas ', True), Cell('Treas ', True)],
        #                            [Cell('Treas ', True), Cell('Treas ', True)]])
        # self.start_room = Room([[1, 1, 1, 1],
        #                         [1, 1, 1, 1],
        #                         [1, 1, 1, 1],
        #                         [1, 1, 1, 1]])
        self.portal_room = Room([[Cell((0, 0, 255), 'Start', True), Cell((0, 0, 255), 'Start ', True)],
                                 [Cell((0, 0, 255), 'Start ', True), Cell((0, 0, 255), 'Start ', True)],
                                 [Cell((0, 0, 255), 'Start ', True), Cell((0, 0, 255), 'Start ', True)],
                                 [Cell((0, 0, 255), 'Start ', True), Cell((0, 0, 255), 'Start ', True)],
                                 [Cell((0, 0, 255), 'Start ', True), Cell((0, 0, 255), 'Start ', True)]])
        self.enemy_rooms = [Room([[3, 3],
                                  [3, 3]]), Room([[5, 5],
                                                  [5, 5]])]
        self.treasure_rooms = [Room([[4, 4],
                                     [4, 4]]), Room([[6, 6],
                                                     [6, 6]])]
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
        delta_x, delta_y = i * self.big_cell_size + x_corner, j * self.big_cell_size + y_corner
        for i in range(len(room)):
            for j in range(len(room[i])):
                self.__field[delta_x + i][delta_y + j] = room[i][j]

    def __create_road(self, start_x, start_y, end_x, end_y):
        start_x, end_x = min(start_x, end_x), max(start_x, end_x)
        start_y, end_y = min(start_y, end_y), max(start_y, end_y)
        if start_x == end_x:
            for i in range(end_y - start_y):
                self.__field[start_x][start_y + i] = Cell((255, 0, 0), 'road', True)
                # self.__field[start_x][start_y + i] = 'x'
        if start_y == end_y:
            for i in range(end_x - start_x):
                self.__field[start_x + i][start_y] = Cell((255, 0, 0), 'road', True)
                # self.__field[start_x + i][start_y] = 'x'

    def generate_field(self):
        map_generator = MapGenerator()
        field, coordinates, coordinates_treasure_rooms = map_generator.generate()
        self.__create_field(field)
        for i in range(len(field)):
            for j in range(len(field[i])):
                field_square = field[i][j]
                if field_square is not None:
                    room = field_square.matrix
                    x_corner, y_corner = self.__find_corner_square(room)
                    self.__add_room_in_field(room, x_corner, y_corner, i, j)
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
        self.print_field(field)
        return self.__field

    def print_field(self, field):
        for row in field:
            print(*row)


class CellSprite(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0, quadrant_size=16, *group):
        super().__init__(*group)
        self.quadrant_size = quadrant_size
        image = self.load_image('1.jpg')
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def load_image(self, name):
        fullname = os.path.join('assets', name)
        if not os.path.isfile(fullname):
            return
        image = pygame.transform.scale(pygame.image.load(fullname), (self.quadrant_size, self.quadrant_size))
        return image

    def update(self):
        self.die()

    def die(self):
        self.kill()


class DrawMap:

    def __init__(self):
        self.screen = None
        self.quadrant_size = 80
        self.width = self.height = 1000
        self.x = self.width // 2
        self.y = self.height // 2
        self.map = CreateFieldMatrix().generate_field()
        self.all_sprites = pygame.sprite.Group()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.update()
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.x - self.width // 2 <= j * self.quadrant_size <= self.x + self.width // 2 and \
                        self.y - self.height // 2 - self.quadrant_size <= \
                        i * self.quadrant_size <= self.y + self.height // 2 + self.quadrant_size:
                    div = self.map[i][j]
                    if div != 0:
                        CellSprite(self.quadrant_size * j - self.x + self.width // 2,
                                   self.quadrant_size * i - self.y + self.height // 2,
                                   self.quadrant_size,
                                   self.all_sprites)
                # pygame.draw.rect(self.screen,
                #                  div.color if div != 0 and type(div) not in (int, str) else (0, 0, 0),
                #                  ((self.quadrant_size * j, self.quadrant_size * i),
                #                   (self.quadrant_size * (j + 1), self.quadrant_size * (i + 1))))

        # self.screen.fill((0, 255, 0))

    def create_window(self):
        pygame.init()
        # size = width, height = len(self.map[0]) * self.quadrant_size, len(self.map) * self.quadrant_size
        size = width, height = self.width, self.height
        self.screen = pygame.display.set_mode(size)
        pygame.display.flip()
        self.draw()
        pygame.display.flip()
        velocity = 100
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x -= velocity
                    if event.key == pygame.K_RIGHT:
                        self.x += velocity
                    if event.key == pygame.K_UP:
                        self.y -= velocity
                    if event.key == pygame.K_DOWN:
                        self.y += velocity
            self.draw()
            self.all_sprites.draw(self.screen)
            pygame.display.update()
        pygame.quit()


# x = MapGenerator()
# for el in x.generate()[0]:
#     print(*el)

# d = CreateFieldMatrix()
# d.generate_field()

draw = DrawMap()
draw.create_window()
