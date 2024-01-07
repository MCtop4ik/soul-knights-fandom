import pygame

from assets import Assets
from map_generation.room_factory import RoomFactory
from settings.constants import Constants
from sprites.sprite_groups import SpriteGroups


class Portal(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = Assets().images['portal']
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        keys = pygame.key.get_pressed()
        if pygame.sprite.spritecollideany(self, SpriteGroups().camera_group):
            if keys[pygame.K_RETURN]:
                self.teleport()

    def teleport(self):
        from level import Level
        Constants().name = "1"
        SpriteGroups().doors_group = pygame.sprite.Group()
        SpriteGroups().walls_group = pygame.sprite.Group()
        SpriteGroups().portal_group = pygame.sprite.Group()
        RoomFactory(Constants().name).load_assets()
        Level().start()
