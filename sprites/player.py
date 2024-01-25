from math import inf

import pygame

from settings.constants import Constants
from sprites.map_sprites.portal import Portal
from sprites.sprite_groups import SpriteGroups


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, player_size, group):
        super().__init__(group)
        self.image = pygame.transform.scale(pygame.image.load('assets/images_test/normal-alpha-leo.png').convert_alpha(),
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
        self.quadrant_size = Constants().quadrant_size
        self.big_cell_size = Constants().big_cell_size

        self.heal_points = inf

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

    def damage(self, damage):
        self.heal_points -= damage
        print(self.heal_points)

    def decrease_enemies_cnt(self, room_coordinates):
        new_uncleared_rooms = []
        for uncleared_room in self.uncleared_rooms:
            new_uncleared_room = uncleared_room
            if uncleared_room[0] == room_coordinates[0] and uncleared_room[1] == room_coordinates[1]:
                new_uncleared_room = (uncleared_room[0], uncleared_room[1], uncleared_room[2] - 1)
            new_uncleared_rooms.append(new_uncleared_room)
        self.uncleared_rooms = new_uncleared_rooms

    def update(self):
        if self.heal_points <= 0:
            self.kill()
            for sprite in SpriteGroups().weapon_group:
                sprite.kill()
            SpriteGroups().weapon_group.update()
            Portal.teleport("2", 'Confrontation.mp3')
        if not self.battle:
            self.not_allowed_through_doors = False
        self.input()

        self.rect.centerx += self.direction.x * self.speed
        while pygame.sprite.spritecollideany(self, SpriteGroups().walls_group):
            self.rect.centerx -= self.direction.x

        self.rect.centery += self.direction.y * self.speed
        while pygame.sprite.spritecollideany(self, SpriteGroups().walls_group):
            self.rect.centery -= self.direction.y

        if pygame.sprite.spritecollideany(self, SpriteGroups().doors_group):
            if self.battle is False:
                self.entered_direction = self.direction
            x, y = (self.rect.centerx // (self.big_cell_size * self.quadrant_size),
                    self.rect.centery // (self.big_cell_size * self.quadrant_size))
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
