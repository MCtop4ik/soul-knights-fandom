import pygame
from math import sin, cos, pi
from assets import Assets
from sprites.sprite_groups import SpriteGroups


class Bullet(pygame.sprite.Sprite):
    def __init__(self, group, angle):
        super().__init__(group)
        self.image = Assets().images['chest']
        self.angle = angle
        print(self.angle)
        self.image = pygame.transform.rotate(self.image, -self.angle - 90)

        self.rect = self.image.get_rect(center=(SpriteGroups().player.rect.x,
                                                SpriteGroups().player.rect.y))
        self.direction = pygame.math.Vector2()
        self.speed = 50


    def angleSolveRadians(self, angle):
        return angle*pi/180

    def update(self):
        convertedAngle = self.angleSolveRadians(self.angle)
        #print(self.speed * sin(self.angle), self.speed * cos(self.angle))
        self.direction.x = cos(convertedAngle)
        self.direction.y = sin(convertedAngle)

        self.rect.center += self.direction * self.speed
        if pygame.sprite.spritecollideany(self, SpriteGroups().walls_group):
            self.kill()
        #self.rect.y += self.speed * sin(self.angle)
        #self.rect.x += self.speed * cos(self.angle)
        #if self.speed * sin(self.angle) == 0 and self.speed * cos(self.angle) == 100:
            #print(self.angle)


