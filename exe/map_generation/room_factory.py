import os
from random import randrange

from assets import Assets
from map_generation.cell import Cell
from map_generation.room import Room
from settings.constants import Constants


class RoomFactory:
    EMPTY_CELL = Constants().EMPTY_CELL

    def __init__(self, name):
        self.name = name
        self.quadrant_size = Constants().quadrant_size

    def read_level(self):
        common = set()
        special = set()

        with open(f"assets/levels/{self.name}.lvl") as file_level_setup:
            level_setup = file_level_setup.readlines()
            for line in level_setup:
                category, data = line.split()[0].strip(), map(str.strip, line.split()[1:])

                if category == 'common':
                    common.update(data)
                if category == 'special':
                    special.update(data)

            if '*' in common:
                common = self.__get_all_file_names_from_directory(
                    directory_path='../assets/rooms/common'
                )
            if '*' in special:
                special = self.__get_all_file_names_from_directory(
                    directory_path=f'assets/rooms/{self.name}'
                )

        start_room = self.load_room(f"assets/rooms/{self.name}/start_room.room")
        portal_room = self.load_room(f"assets/rooms/{self.name}/portal_room.room")
        enemy_rooms = list(filter(
            lambda room: room is not None, [
                                               self.load_room(f"assets/rooms/{self.name}/{name}")
                                               if name.split('.')[1:] == ['enemy_room', 'special', 'room']
                                               else None
                                               for name in special
                                           ] + [
                                               self.load_room(f"assets/rooms/common/{name}")
                                               if name.split('.')[1:] == ['enemy_room', 'common', 'room']
                                               else None
                                               for name in common
                                           ]))
        treasury_rooms = list(filter(
            lambda room: room is not None, [
                                               self.load_room(f"assets/rooms/{self.name}/{name}")
                                               if name.split('.')[1:] == ['treasure_room', 'special', 'room']
                                               else None
                                               for name in special
                                           ] + [
                                               self.load_room(f"assets/rooms/common/{name}")
                                               if name.split('.')[1:] == ['treasure_room', 'common', 'room']
                                               else None
                                               for name in common
                                           ]))
        return {
            'start_room': start_room,
            'portal_room': portal_room,
            'enemy_rooms': enemy_rooms,
            'treasury_rooms': treasury_rooms
        }

    @staticmethod
    def __get_all_file_names_from_directory(directory_path):
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        return files

    def load_assets(self):
        new_abbr = dict()

        with open(f"assets/rooms/{self.name}/signed_pictures.special.sprite") as file_level_setup:
            images_setup = file_level_setup.readlines()
            for line in images_setup:
                key, path = line.split(' -> ')
                new_abbr[int(key)] = f'level_{self.name}/{path.strip()}'

        Assets().load_abbr(new_abbr)

    def load_room(self, path):
        with open(path) as file:
            room = file.readline().split()
            label, room_width, room_height, room_floor = room[0], int(room[1]), int(room[2]), room[3:]

            loaded_room = [[self.EMPTY_CELL for _ in range(room_width)]
                           for _ in range(room_height)]
            for i in range(room_height):
                for j in range(room_width):
                    loaded_room[i][j] = Cell(int(room_floor[randrange(len(room_floor))]), label)

            return Room(loaded_room)

    def get_road_images(self):
        with open(f"assets/rooms/{self.name}/sprites.road") as file_level_setup:
            return list(map(int, file_level_setup.readline().split()))

    def get_wall_images(self):
        with open(f"assets/rooms/{self.name}/sprites.wall") as file_level_setup:
            return list(map(int, file_level_setup.readline().split()))
