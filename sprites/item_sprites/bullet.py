import pygame
from math import sin, cos, pi
from assets import Assets
from sprites.sprite_groups import SpriteGroups


class Bullet(pygame.sprite.Sprite):
    def __init__(self, group, angle):
        super().__init__(group)
        self.image = Assets().images['chest']
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, -self.angle - 90)

        self.rect = self.image.get_rect(center=(SpriteGroups().player.rect.x,
                                                SpriteGroups().player.rect.y))
        self.direction = pygame.math.Vector2()
        self.speed = 15

    @staticmethod
    def angle_solve_radians(angle):
        return angle * pi / 180

    def update(self):
        converted_angle = self.angle_solve_radians(self.angle)
        self.direction.x = cos(converted_angle)
        self.direction.y = sin(converted_angle)

        self.rect.center += self.direction * self.speed
        if pygame.sprite.spritecollideany(self, SpriteGroups().walls_group):
            self.kill()
