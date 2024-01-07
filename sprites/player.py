import pygame

from settings.constants import Constants
from settings.game_state_manager import GameStateManager
from sprites.sprite_groups import SpriteGroups


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, player_size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load('assets/images_test/player.png').convert_alpha(),
                                            player_size)
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.speed = Constants().speed

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self):
        keys = pygame.key.get_pressed()
        self.input()
        self.rect.center += self.direction * self.speed
        while pygame.sprite.spritecollideany(self, SpriteGroups().walls_group):
            self.rect.center -= self.direction
        if pygame.sprite.spritecollideany(self, SpriteGroups().portal_group):
            if keys[pygame.K_RETURN]:
                if GameStateManager().next_level is False:
                    GameStateManager().next_level = True
