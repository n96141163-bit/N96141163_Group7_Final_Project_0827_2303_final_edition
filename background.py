import pygame
from Config import *
import Glo


class Background:
    def __init__(self, image_path, speed=1):
        self.speed = speed
        self.image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT + 1800))

        # 取得實際圖片高度，之後用這個值計算循環
        self.image_height = self.image.get_height()

        # 兩張背景圖，一張在上面，一張接在下面
        self.y1 = 0
        self.y2 = -self.image_height

    def update(self):
        self.y1 += self.speed * Glo.SPEED_RATE
        self.y2 += self.speed * Glo.SPEED_RATE

        # 如果背景完全離開畫面，就把它放回最上面
        if self.y1 >= SCREEN_HEIGHT:
            self.y1 = self.y2 - self.image_height
        if self.y2 >= SCREEN_HEIGHT:
            self.y2 = self.y1 - self.image_height

    def draw(self, screen):
        screen.blit(self.image, (0, self.y1))
        screen.blit(self.image, (0, self.y2))




'''
class Background:
    def __init__(self, image_path, speed=1):
        self.speed = speed 
        self.image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # 兩張背景圖，一張在上面，一張接在下面
        self.y1 = 0
        self.y2 = -SCREEN_HEIGHT

    def update(self):
        self.y1 += self.speed * Glo.SPEED_RATE
        self.y2 += self.speed * Glo.SPEED_RATE

        # 如果背景完全離開畫面，就把它放回最上面
        if self.y1 >= SCREEN_HEIGHT:
            self.y1 = self.y2 - SCREEN_HEIGHT
        if self.y2 >= SCREEN_HEIGHT:
            self.y2 = self.y1 - SCREEN_HEIGHT

    def draw(self, screen):
        screen.blit(self.image, (0, self.y1))
        screen.blit(self.image, (0, self.y2))
'''

