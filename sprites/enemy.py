import pygame

from assets import Assets
from settings.constants import Constants
from sprites.sprite_groups import SpriteGroups


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = Assets().images['enemy']
        self.rect = self.image.get_rect(center=pos)
        self.pos = pos
        self.direction = pygame.math.Vector2()
        self.speed = 15

    def get_direction(self):
        x_player, y_player = SpriteGroups().player.get_player_coordinates()

        # if keys[pygame.K_UP] or keys[pygame.K_w]:
        #     self.direction.y = -1
        # elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        #     self.direction.y = 1
        # else:
        #     self.direction.y = 0
        #
        # if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        #     self.direction.x = 1
        # elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        #     self.direction.x = -1
        # else:
        #     self.direction.x = 0

    def update(self):
        self.get_direction()
        self.rect.center += self.direction * self.speed

        while pygame.sprite.spritecollideany(self, SpriteGroups().walls_group):
            self.rect.center -= self.direction
