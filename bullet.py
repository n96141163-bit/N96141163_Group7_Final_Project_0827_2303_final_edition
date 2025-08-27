import pygame
from Config import *
import Glo

class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_type, x, y, speedx, speedy, damage=10):
        super().__init__()
        self.x = x
        self.y = y
        self.bullet_type = bullet_type      #新增
        # self.rect = self.image.get_rect(center=(self.x, self.y))
        self.speedx = speedx
        self.speedy = speedy
        self.damage = damage
        self.frame = 0
        self.animation_time = 0
        self.animation_delay = 50
        self.is_animation = False
        self.animation = []
        self.image = None
        self.rect = None


    def update(self):
        if self.bullet_type == "boss3" or self.bullet_type == "boss3-1":
            self.rect.y -= self.speedy*Glo.SPEED_RATE
            self.rect.x += self.speedx*Glo.SPEED_RATE
        else:
            self.rect.y -= self.speedy
            self.rect.x += self.speedx

        if self.rect.y < -15 or self.y > SCREEN_HEIGHT + 15:
            self.kill()

        if self.is_animation and self.animation:
            now = pygame.time.get_ticks()
            if now - self.animation_time > self.animation_delay:
                self.frame = (self.frame + 1) % len(self.animation)
                self.image = self.animation[self.frame]
                self.animation_time = now


