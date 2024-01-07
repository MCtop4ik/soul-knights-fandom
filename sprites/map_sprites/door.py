import pygame

from assets import Assets


class Door(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = Assets().images['door']
        self.rect = self.image.get_rect(center=pos)
