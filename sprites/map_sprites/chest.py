import pygame

from assets import Assets
from sprites.sprite_groups import SpriteGroups


class Chest(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = Assets().images['chest']
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        keys = pygame.key.get_pressed()
        if pygame.sprite.spritecollideany(self, SpriteGroups().camera_group):
            if keys[pygame.K_RETURN]:
                print('chest opened')

