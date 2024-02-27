from dataclasses import dataclass
from typing import List

from map_generation.cell import Cell


@dataclass(frozen=True)
class Room:
    matrix: List[List[Cell]]
