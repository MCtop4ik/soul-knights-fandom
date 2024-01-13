import pygame

from settings.constants import Constants
from sprites.sprite_groups import SpriteGroups


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, player_size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load('assets/images_test/player.png').convert_alpha(),
                                            player_size)
        self.rect = self.image.get_rect(center=pos)
        self.pos = pos
        self.direction = pygame.math.Vector2()
        self.speed = Constants().speed
        self.battle = False
        self.uncleared_rooms = []
        self.not_allowed_through_doors = False
        self.entered_direction = (0, 0)
        self.finished_direction = (0, 0)

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
        self.input()
        self.rect.center += self.direction * self.speed

        while pygame.sprite.spritecollideany(self, SpriteGroups().walls_group):
            self.rect.center -= self.direction

        if pygame.sprite.spritecollideany(self, SpriteGroups().doors_group):
            if self.battle is False:
                self.entered_direction = self.direction
            x, y = (self.rect.centerx // (Constants().big_cell_size * Constants().quadrant_size),
                    self.rect.centery // (Constants().big_cell_size * Constants().quadrant_size))
            for uncleared_room in self.uncleared_rooms:
                if x == uncleared_room[0] and y == uncleared_room[1]:
                    if uncleared_room[2] > 0:
                        self.battle = True
                    else:
                        self.battle = False
        else:
            if self.battle:
                self.finished_direction = self.direction
                self.not_allowed_through_doors = True

        while pygame.sprite.spritecollideany(self, SpriteGroups().doors_group) and self.not_allowed_through_doors:
            self.rect.center -= self.direction

    def get_player_coordinates(self):
        return self.rect.center

    def set_uncleared_rooms(self, uncleared_rooms):
        self.uncleared_rooms = uncleared_rooms
