import pygame

from assets import Assets


class Portal(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = Assets().images['portal']
        self.rect = self.image.get_rect(center=pos)
