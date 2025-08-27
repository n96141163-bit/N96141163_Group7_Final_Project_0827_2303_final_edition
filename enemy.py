import pygame
import random
from Config import *
from bullet_factory import BulletFactory
from spaceship import Spaceship

import Glo


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, animation, bullet_group, bullet_type="enemy1", value=100, speedx_range=(-2, 2), speedy_range=(2, 4)):
        super().__init__()
        self.x = x
        self.y = y
        self.animation = animation
        self.image = self.animation[0]
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.speedx = random.randint(*speedx_range)#*Glo.SPEED_RATE
        self.speedy = random.randint(*speedy_range)#*Glo.SPEED_RATE
        self.change_direction_time = 0
        self.change_direction_delay = 1200
        self.bullet_group = bullet_group
        self.bullet_time = 0
        self.min_delay = 1000   # 最短間隔（毫秒）
        self.max_delay = 2000  # 最長間隔（毫秒）
        self.bullet_delay = random.randint(self.min_delay, self.max_delay)
        self.bullet_type = bullet_type
        self.value = value
        self.frame = 0
        self.animation_time = 0
        self.animation_delay = 50
        
        self.mark = 1
        
        if self.rect.centerx < SCREEN_WIDTH/2 and self.rect.centerx >= 150:
            self.speedy += 14 * Glo.SPEED_RATE
        elif self.rect.centerx < 150:
            self.speedy += 3 * Glo.SPEED_RATE
        elif self.rect.centerx >= SCREEN_WIDTH/2 :
            self.speedy += 10 * max(Glo.SPEED_RATE-1, 0)



    def constrain_movement(self):
        if self.rect.left <= 150 or self.rect.right >= SCREEN_WIDTH-150 or self.rect.left == SCREEN_WIDTH/2 or self.rect.right == SCREEN_WIDTH/2:
            self.speedx = -self.speedx
            #self.rect.x -= self.speedx
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
            
        
        if self.mark != Glo.SPEED_RATE and Glo.SPEED_RATE != 0:
            if self.rect.centerx < SCREEN_WIDTH/2 and self.rect.centerx >= 150:
                self.speedy += 14 * (Glo.SPEED_RATE-self.mark)
            elif self.rect.centerx < 150:
                self.speedy += 3 * (Glo.SPEED_RATE-self.mark)
            elif self.rect.centerx >= SCREEN_WIDTH/2 :
                self.speedy += 10 * (Glo.SPEED_RATE-self.mark)
            self.mark = Glo.SPEED_RATE
        elif self.mark != Glo.SPEED_RATE and Glo.SPEED_RATE == 0:
            if self.rect.centerx < SCREEN_WIDTH/2 and self.rect.centerx >= 150:
                self.speedy += 14 * (Glo.SPEED_RATE-self.mark) + 4
            elif self.rect.centerx < 150:
                self.speedy += 3 * (Glo.SPEED_RATE-self.mark) - 10
            elif self.rect.centerx >= SCREEN_WIDTH/2 :
                self.speedy += 10 * (Glo.SPEED_RATE-self.mark) - 4
            self.mark = Glo.SPEED_RATE
            
            
           
           

    def change_direction(self):
        now = pygame.time.get_ticks()
        if now - self.change_direction_time > self.change_direction_delay:
            self.speedx = self.speedx * random.choice([-1, 1])
            self.change_direction_time = pygame.time.get_ticks()

    def shoot_bullet(self):
        if self.bullet_type == "police":
            now = pygame.time.get_ticks()
            if now - self.bullet_time > self.bullet_delay:
                bullet = BulletFactory.create(self.bullet_type, self.rect.centerx, self.rect.bottom)
                self.bullet_group.add(bullet)
                self.bullet_time = now
                self.bullet_delay = random.randint(self.min_delay, self.max_delay)
        pass

    def update(self):
        self.rect.centerx -= self.speedx
        self.rect.centery += self.speedy
        self.constrain_movement()
        self.change_direction()
        self.shoot_bullet()
        self.bullet_group.update()
        
        

        now = pygame.time.get_ticks()
        if now - self.animation_time > self.animation_delay:
            self.frame += 1
            self.animation_time = pygame.time.get_ticks()
            if self.frame == len(self.animation):
                self.frame = 0
            else:
                self.image = self.animation[self.frame]

