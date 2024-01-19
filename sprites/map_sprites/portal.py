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
        if self.rect.colliderect(SpriteGroups().player.rect.inflate(
                Constants().quadrant_size * 3, Constants().quadrant_size * 3)):
            if keys[pygame.K_RETURN]:
                self.teleport("1")

    @staticmethod
    def teleport(level_name):
        from level import Level
        Constants().name = level_name
        SpriteGroups().doors_group = pygame.sprite.Group()
        SpriteGroups().walls_group = pygame.sprite.Group()
        SpriteGroups().portal_group = pygame.sprite.Group()
        SpriteGroups().chests_group = pygame.sprite.Group()
        SpriteGroups().enemies_group = pygame.sprite.Group()
        SpriteGroups().inventory_group = pygame.sprite.Group()
        RoomFactory(Constants().name).load_assets()
        Level().start()
