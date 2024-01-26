import pygame

from assets import Assets


class Box(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = Assets().images['box']
        self.rect = self.image.get_rect(center=pos)
        self.health = 100

    def damage(self, damage):
        self.health -= damage

    def update(self):
        if self.health <= 0:
            self.kill()
