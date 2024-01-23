import random


class BoxStructures:
    box_types = {
        'standard': 10,
        'poison': 20,
        'flame': 30,
        'ice': 40,
        'light': 50,
        'dark': 60
    }
    box_structures = [[['standard', 'standard'], ['standard', 'standard']]]

    def random_box_structure(self):
        return self.box_structures[random.randint(0, len(self.box_structures) - 1)]
