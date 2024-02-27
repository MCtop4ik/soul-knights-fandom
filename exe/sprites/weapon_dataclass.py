from dataclasses import dataclass


@dataclass
class Weapon:
    id: int
    weapon_name: str
    fire_damage: int
    cut_off: int
    offset_time: int
    image_name: str
    offset_x: int
    offset_y: int
    size_x: int
    size_y: int
    bullet_id: int
