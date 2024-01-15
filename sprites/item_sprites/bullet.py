import pygame
from math import sin, cos, pi
from assets import Assets
from sprites.sprite_groups import SpriteGroups


class Bullet(pygame.sprite.Sprite):
    def __init__(self, group, angle, offset_x, offset_y, start_coordinates, sender, asset_id, fire_damage):
        super().__init__(group)
        self.assetID = asset_id
        self.image = Assets().images[self.assetID]
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, -self.angle - 90)
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.rect = self.image.get_rect(center=start_coordinates)
        self.rect.x += offset_x
        self.rect.y += offset_y
        self.direction = pygame.math.Vector2()
        self.sender = sender
        self.speed = 15
        self.fire_damage = fire_damage

    @staticmethod
    def angle_solve_radians(angle):
        return angle * pi / 180

    def update(self):
        converted_angle = self.angle_solve_radians(self.angle)
        self.direction.x = cos(converted_angle)
        self.direction.y = sin(converted_angle)

        self.rect.center += self.direction * self.speed
        if self.rect.colliderect(SpriteGroups().player.rect):
            if self.sender == 'enemy':
                SpriteGroups().player.damage(self.fire_damage)
        enemy = pygame.sprite.spritecollideany(self, SpriteGroups().enemies_group)
        if enemy:
            if self.sender == 'player':
                enemy.damage(self.fire_damage)
        if (pygame.sprite.spritecollideany(self, SpriteGroups().walls_group) or
                pygame.sprite.spritecollideany(self, SpriteGroups().doors_group) or
                (pygame.sprite.spritecollideany(self, SpriteGroups().enemies_group) and self.sender == 'player') or
                self.rect.colliderect(SpriteGroups().player.rect) and self.sender == 'enemy'):
            self.kill()
