from level import Level
from map_generation.room_factory import RoomFactory
from settings.constants import Constants

if __name__ == '__main__':
    RoomFactory(Constants().name).load_assets()
    Level().start()