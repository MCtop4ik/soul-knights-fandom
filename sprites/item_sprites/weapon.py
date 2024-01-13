import pygame
import sqlite3
from assets import Assets
from sprites.item_sprites.bullet import Bullet
from sprites.sprite_groups import SpriteGroups


class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.angle = 0
        self.offset_y = 20
        self.offset_x = 20
        self.offset_time_ms = 10
        self.last_shoot_time = 0
        self.rect = None
        self.image = None
        self.pos = pos
        self.group = group
        self.defaultWeaponBaseID = "test_weapon"
        self.currentWeaponInt = 1
        self.changeWeapon(self.defaultWeaponBaseID)

    def initWeapon(self, offset_time, offset_x, offset_y, image_id):
        self.image = Assets().images[image_id]
        self.rect = self.image.get_rect(center=self.pos)
        self.rect.x += offset_x
        self.rect.y = offset_y
        self.last_shoot_time = 0
        self.offset_time_ms = offset_time
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.angle = 0

    def update(self):
        keys = pygame.key.get_pressed()
        self.rect = SpriteGroups().player.rect.copy()
        self.rect.x += self.offset_x
        self.rect.y += self.offset_y
        if keys[pygame.K_SPACE] and pygame.time.get_ticks() - self.last_shoot_time > self.offset_time_ms:
            self.shoot()
            self.last_shoot_time = pygame.time.get_ticks()

        if keys[pygame.K_1]:
            if self.currentWeaponInt != 1:
                self.currentWeaponInt = 1
                print("a")
                self.changeWeapon("test_weapon")
        elif keys[pygame.K_2]:
            if self.currentWeaponInt != 2:
                self.currentWeaponInt = 2
                print("b")
                self.changeWeapon("test_weapon_2")

    def shoot(self):
        Bullet(SpriteGroups().bullets_group, self.angle, self.offset_x + 50, self.offset_y + 60, (SpriteGroups().player.rect.x,
                                                SpriteGroups().player.rect.y), 'chest')
        self.angle = (self.angle + 10) % 360

    def changeWeapon(self, baseID):
        connection = Assets.load_base()
        cursor = connection.cursor()
        sql_select_query = """select * from weapons where id = ?"""
        cursor.execute(sql_select_query, (baseID,))
        data = cursor.fetchone()
        self.initWeapon(data[1], data[2], data[3], data[4])
        connection.close()
