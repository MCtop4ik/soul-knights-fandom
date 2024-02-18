from level import Level
from map_generation.room_factory import RoomFactory
from settings.constants import Constants
from settings.player_state import PlayerState

if __name__ == '__main__':
    Constants().name = PlayerState().levels[PlayerState().level_index]
    RoomFactory(Constants().name).load_assets()
    Level().start()
