import pygame

from assets import Assets
from sprites.sprite_groups import SpriteGroups


class DroppedWeapon(pygame.sprite.Sprite):
    def __init__(self, item, pos, group):
        super().__init__(group)
        self.image = Assets().images[item.image_name]
        self.rect = self.image.get_rect(center=pos)
        self.pos = pos
        self.item = item
        self.last_click = pygame.time.get_ticks()

    def update(self):
        from sprites.inventory import InventoryV2
        keys = pygame.key.get_pressed()
        if pygame.sprite.spritecollideany(self, SpriteGroups().camera_group):
            if keys[pygame.K_RETURN] and pygame.time.get_ticks() - self.last_click > 1000:
                self.last_click = pygame.time.get_ticks()
                dropped_item = InventoryV2().add_item_in_inventory(self.item)
                if dropped_item:
                    self.image = Assets().images[dropped_item.image_name]
                    self.item = dropped_item
                else:
                    self.kill()
