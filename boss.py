import pygame
import random
from Config import *
from bullet_factory import BulletFactory


boss_images = {
        "boss1": pygame.transform.scale(
            pygame.image.load("Image/boss1.png"), (120, 120)), 
        "boss2": pygame.transform.scale(
            pygame.image.load("Image/boss2.png"), (120, 120)), 
        "boss3": pygame.transform.scale(
            pygame.image.load("Image/boss3.png"), (150, 150)), 
            }


class Boss1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = boss_images["boss1"]
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        self.speedx = 3
        self.speedy = 3
        self.change_direction_time = pygame.time.get_ticks()
        self.change_direction_delay = 600
        self.first_generate_time = pygame.time.get_ticks()
        self.value = 49
        self.boundary = 100
        self.hp = 50
        self.hp_max = 50
        self.bullet_group = pygame.sprite.Group()
        self.bullet_time = 0
        self.bullet_delay = 1000
        

    def constrain_movement(self):
        '''
        if self.rect.left < 0 or self.rect.right >= SCREEN_WIDTH:
            self.speedx = -self.speedx
            
        if self.rect.bottom < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speedy = -self.speedy
            #self.rect.centery = 0
            
        now = pygame.time.get_ticks()
        '''
            
       
        
        
        if self.rect.left < self.boundary or self.rect.right >= SCREEN_WIDTH-self.boundary:
            self.speedx = -self.speedx
        if self.rect.bottom >= self.rect.height+100:
            self.rect.bottom = self.rect.height+100
        now = pygame.time.get_ticks()
        if now - self.first_generate_time > (self.rect.height+100)/(self.speedy*FPS)*1000:
            if self.rect.top <= 20:
                self.speedy = -self.speedy
                
        

    def change_direction(self):
        now = pygame.time.get_ticks()
        if now - self.change_direction_time > self.change_direction_delay:
            self.speedx = self.speedx * random.choice([-1, 1])
            self.speedy = self.speedy * random.choice([-1, 1])
            '''
            if now - self.first_generate_time > self.rect.height/(self.speedy*FPS)*1000:
                self.speedy = self.speedy * random.choice([-1, 1])
                '''
            self.change_direction_time = pygame.time.get_ticks()

    def shoot_bullet(self):
        '''
        now = pygame.time.get_ticks()
        if now - self.bullet_time >= self.bullet_delay:
            self.bullet_group.add(BulletFactory.create("boss1", self.rect.centerx-65, self.rect.bottom-20))
            self.bullet_group.add(BulletFactory.create("boss1", self.rect.centerx+65, self.rect.bottom-20))
            self.bullet_time = pygame.time.get_ticks()
            '''
        pass


    def update(self):
        self.rect.centerx -= self.speedx
        self.rect.centery += self.speedy
        self.change_direction()
        self.constrain_movement()
        self.shoot_bullet()
        self.bullet_group.update()

    def draw_hp(self, surface):
        hp = self.rect.width*(self.hp/self.hp_max)
        pygame.draw.rect(surface, RED, (self.rect.left, self.rect.top-10, hp, 15), 0)
        pygame.draw.rect(surface, WHITE, (self.rect.left, self.rect.top-10, self.rect.width, 15), 2)



class Boss2(Boss1):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speedx = 4
        self.speedy = 4
        self.image = boss_images["boss2"]
        self.hp = 100
        self.hp_max = 100
        self.value = 49
        self.change_direction_delay = 400
        self.bullet_delay = 1500


    def shoot_bullet(self):
        now = pygame.time.get_ticks()
        if now - self.bullet_time >= self.bullet_delay:
            self.bullet_group.add(BulletFactory.create("boss2-1", self.rect.centerx-65, self.rect.bottom-10, speedx_override=-1))
            self.bullet_group.add(BulletFactory.create("boss2-1", self.rect.centerx+65, self.rect.bottom-10, speedx_override=1))
            self.bullet_group.add(BulletFactory.create("boss2", self.rect.centerx, self.rect.bottom-10))
            self.bullet_time = pygame.time.get_ticks()
            
class Boss3(Boss1):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speedx = 4
        self.speedy = 4
        self.image = boss_images["boss3"]
        self.hp = 150
        self.hp_max = 150
        self.value = 49
        self.change_direction_delay = 400
        self.bullet_delay = 1500


    def shoot_bullet(self):
        now = pygame.time.get_ticks()
        if now - self.bullet_time >= self.bullet_delay:
            '''
            self.bullet_group.add(BulletFactory.create("boss2-1", self.rect.centerx-65, self.rect.bottom-10, speedx_override=-1))
            self.bullet_group.add(BulletFactory.create("boss2-1", self.rect.centerx+65, self.rect.bottom-10, speedx_override=1))
            '''
            self.bullet_group.add(BulletFactory.create("boss3", random.randrange(self.rect.centerx-140, self.rect.centerx+140), self.rect.bottom-10))
            self.bullet_group.add(BulletFactory.create("boss3-1", random.randrange(self.rect.centerx-140, self.rect.centerx+140), self.rect.bottom-10))
            self.bullet_time = pygame.time.get_ticks()
            
            
            
            