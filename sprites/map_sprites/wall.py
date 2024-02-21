from random import randrange

import pygame

from assets import Assets


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        print(Assets().wall_image_ids)
        self.image = Assets().images[
            Assets().wall_image_ids[
                randrange(len(Assets().wall_image_ids))
            ]
        ]
        self.rect = self.image.get_rect(center=pos)
