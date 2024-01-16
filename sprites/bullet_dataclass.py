from dataclasses import dataclass


@dataclass
class Bullet:
    id: int
    name: str
    speed: int
    fire_damage: int
    offset_x: int
    offset_y: int
    asset_id: str
