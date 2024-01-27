import pygame

from assets import Assets


class Energy(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = Assets().images['energy']
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        pass
