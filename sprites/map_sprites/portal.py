import pygame

from windows import end_screen
from assets import Assets
from map_generation.room_factory import RoomFactory
from settings.constants import Constants
from settings.player_state import PlayerState
from sprites.sprite_groups import SpriteGroups
from windows.end_screen import EndScreen


class Portal(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = Assets().images['portal']
        self.rect = self.image.get_rect(center=pos)
        self.state = 0
        self.last_tick = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.last_tick > 90:
            self.state = self.state % 8
            self.image = Assets().images[f'portal_{self.state}']
            self.state += 1
            self.last_tick = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        if self.rect.colliderect(SpriteGroups().player.rect.inflate(
                Constants().quadrant_size * 3, Constants().quadrant_size * 3)):
            if keys[pygame.K_RETURN]:
                PlayerState().level_index += 1
                if PlayerState().level_index == len(PlayerState().levels):
                    EndScreen().run()
                    SpriteGroups().clear_level_sprites()
                    return
                self.teleport(PlayerState().levels[PlayerState().level_index], 'FallingMysts.mp3')

    @staticmethod
    def teleport(level_name, music_name):
        from level import Level
        Constants().name = level_name
        Constants().music = music_name
        SpriteGroups().clear_level_sprites()
        RoomFactory(Constants().name).load_assets()
        Level().start()
