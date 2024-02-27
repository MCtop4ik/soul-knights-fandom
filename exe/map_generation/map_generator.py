from random import randint, randrange

from settings.constants import Constants


class MapGenerator:

    def __init__(self, rooms):
        self.start_room = rooms['start_room']
        self.portal_room = rooms['portal_room']
        self.enemy_rooms = rooms['enemy_rooms']
        self.treasure_rooms = rooms['treasury_rooms']
        self.__min_enemies_rooms = Constants().min_enemies_rooms
        self.__max_enemies_rooms = Constants().max_enemies_rooms
        self.__max_treasuries_rooms = Constants().max_treasuries_rooms
        self.rooms_amount = 2 + self.__max_treasuries_rooms + self.__max_enemies_rooms
        self.__rooms = self.__create_rooms_matrix()
        self.__all_coordinates = []
        self.__coordinates = [(self.rooms_amount + 1, self.rooms_amount + 1)]
        self.__coordinates_for_treasure_room = []
        self.enemy_room_sizes = []

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
            add_room = rooms[randrange(len(rooms))]
            self.__rooms[x_gen][y_gen] = add_room
            if rooms == self.enemy_rooms:
                self.enemy_room_sizes.append((len(add_room.matrix[0]), len(add_room.matrix)))

    def __create_enemy_rooms(self):
        enemies_rooms_number = randint(self.__min_enemies_rooms, self.__max_enemies_rooms)
        self.__create_room(enemies_rooms_number, self.enemy_rooms)

    def __create_portal_room(self):
        self.__create_room(1, [self.portal_room])

    def __create_treasure_rooms(self):
        cnt_treasuries = 0
        left_shift = 1
        right_shift = 1
        chance = Constants().chance
        iters_for_chance = Constants().iters_for_chance

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
        return self.__rooms, self.__coordinates, self.__coordinates_for_treasure_room, self.enemy_room_sizes
