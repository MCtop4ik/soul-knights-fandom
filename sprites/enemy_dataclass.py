from dataclasses import dataclass


@dataclass
class Enemy:
    id: int
    heal_points: int
    name: str
    speed: int
    fire_radius_coefficient: int
    offset_shoot_time: int
    offset_moved_time: int
    cut_off: int
    asset_id: str
