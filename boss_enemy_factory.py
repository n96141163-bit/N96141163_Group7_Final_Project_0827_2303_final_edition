# boss_enemy_factory.py
import pygame
from enemy import Enemy

class BossEnemyFactory:
    enemy_images = {}
    max_enemies = 35   # ✅ 場上同時存在的小怪數量上限

    @staticmethod
    def load_images():
        BossEnemyFactory.enemy_images = {
            "boss3_1": [pygame.transform.scale(
                pygame.image.load("Image/enemy/boss3_1.png"), (80, 80))],
            
            "boss3_2": [pygame.transform.scale(
                pygame.image.load("Image/enemy/boss3_2.png"), (100, 100))],
            
            "boss3_3": [pygame.transform.scale(
                pygame.image.load("Image/enemy/boss3_3.png"), (120, 120))]
        }

    @staticmethod
    def create(enemy_type, x, y, bullet_group, current_enemies=0):
        if current_enemies >= BossEnemyFactory.max_enemies:
            print("[BossEnemyFactory] 小怪數量已達上限，不再生成")
            return None

        if enemy_type in BossEnemyFactory.enemy_images:
            return Enemy(x, y,
                         animation=BossEnemyFactory.enemy_images[enemy_type],
                         bullet_group=bullet_group,
                         bullet_type="enemy1",  # 先沿用enemy1的子彈
                         value=49,
                         speedy_range=(2, 5))

