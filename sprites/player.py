import pygame

from settings.constants import Constants
from settings.player_state import PlayerState
from sprites.map_sprites.portal import Portal
from sprites.sprite_groups import SpriteGroups


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, player_size, level, group):
        super().__init__(group)
        self.image = pygame.transform.scale(
            pygame.image.load('assets/images_test/normal-alpha-leo.png').convert_alpha(),
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
        self.level = level

        self.heal_points = PlayerState().health
        self.energy = PlayerState().energy
        self.money = PlayerState().money
        self.player_name = PlayerState().character

        self.state = 0
        self.last_tick = pygame.time.get_ticks()
        self.look_side = 'right'

    def input(self):
        keys = pygame.key.get_pressed()
        from assets import Assets
        if pygame.time.get_ticks() - self.last_tick > 90:
            if any(keys):
                if self.state < 8:
                    self.state = 8
                self.state = self.state % 16
            else:
                if self.state > 8:
                    self.state = 0
                self.state = self.state % 8
            self.image = Assets().images[f'{self.player_name}_{self.state}']
            if self.look_side == 'left':
                self.image = pygame.transform.flip(self.image, True, False)
            self.state += 1
            self.last_tick = pygame.time.get_ticks()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.look_side = 'right'
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.look_side = 'left'
        else:
            self.direction.x = 0

    def damage(self, damage):
        self.heal_points -= damage
        PlayerState().health = self.heal_points

    def decrease_enemies_cnt(self, room_coordinates):
        new_uncleared_rooms = []
        for uncleared_room in self.uncleared_rooms:
            new_uncleared_room = uncleared_room
            if uncleared_room[0] == room_coordinates[0] and uncleared_room[1] == room_coordinates[1]:
                new_uncleared_room = (uncleared_room[0], uncleared_room[1], uncleared_room[2] - 1)
            new_uncleared_rooms.append(new_uncleared_room)
        self.uncleared_rooms = new_uncleared_rooms

    def update(self):
        stay_cell = self.level[self.get_player_coordinates()[1] // self.quadrant_size][self.get_player_coordinates()[0] // self.quadrant_size]
        if self.heal_points <= 0:
            self.kill()
            for sprite in SpriteGroups().weapon_group:
                sprite.kill()
            SpriteGroups().weapon_group.update()
            PlayerState().health = 500
            PlayerState().energy = 300
            Portal.teleport(PlayerState().levels[0], 'Confrontation.mp3')
        if not self.battle:
            self.not_allowed_through_doors = False
        self.input()
        self.rect.centerx += self.direction.x * self.speed
        while (pygame.sprite.spritecollideany(self, SpriteGroups().walls_group) or
               pygame.sprite.spritecollideany(self, SpriteGroups().boxes_group)):
            self.rect.centerx -= self.direction.x
        self.rect.centery += self.direction.y * self.speed
        while (pygame.sprite.spritecollideany(self, SpriteGroups().walls_group) or
               pygame.sprite.spritecollideany(self, SpriteGroups().boxes_group)):
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
            if self.battle and stay_cell.name == 'Enemy':
                self.finished_direction = self.direction
                self.not_allowed_through_doors = True
            else:
                self.battle = False

        while pygame.sprite.spritecollideany(self, SpriteGroups().doors_group) and self.not_allowed_through_doors:
            self.rect.center -= self.direction
        energy_obj = pygame.sprite.spritecollideany(self, SpriteGroups().energy_group)
        if energy_obj:
            self.energy += 8
            energy_obj.kill()
        coins_obj = pygame.sprite.spritecollideany(self, SpriteGroups().coins_group)
        if coins_obj:
            self.money += coins_obj.get_amount()
            coins_obj.kill()
        PlayerState().energy = min(self.energy, PlayerState().max_energy)
        PlayerState().money = self.money

    def get_player_coordinates(self):
        return self.rect.center

    def set_uncleared_rooms(self, uncleared_rooms):
        self.uncleared_rooms = uncleared_rooms

    def use_energy(self, amount):
        if self.energy - amount >= 0:
            self.energy -= amount
            PlayerState().energy = self.energy
            return True
        return False
