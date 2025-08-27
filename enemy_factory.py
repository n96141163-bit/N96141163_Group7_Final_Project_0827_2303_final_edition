import pygame
from enemy import Enemy
import random


class EnemyFactory:
    enemy_images = {}
    enemy_variants = ["-0", "-1", "-2", "-3", "-4", "-5"]
    enemy_variants2 = ["-0", "-1", "-2"]

    @staticmethod
    def load_images(dummy_index=None):  # 加入兼容參數
        EnemyFactory.enemy_images = {
            "enemy1-0": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy1/enemy0{i}.png"), (60, 120)) for i in range(5)],
            "enemy1-1": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy1/enemy1{i}.png"), (60, 120)) for i in range(5)],
            "enemy1-2": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy1/enemy2{i}.png"), (60, 120)) for i in range(5)],
            "enemy1-3": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy1/enemy3{i}.png"), (60, 120)) for i in range(5)],
            "enemy1-4": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy1/enemy4{i}.png"), (35, 55)) for i in range(5)],
            "enemy1-5": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy1/enemy50.png"), (80, 180)) ],
            "police": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy1/enemyP{i}.png"), (60, 120)) for i in range(5)],
            "enemy2-0": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy2/2walkers{i}.png"), (35, 70)) for i in range(0, 20, 2)],
            "enemy2-1": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy2/3walkers{i}.png"), (35, 70)) for i in range(0, 20, 2)],
            "enemy2-2": [pygame.transform.scale(
                pygame.image.load(f"Image/enemy/enemy2/4walkers{i}.png"), (35, 70)) for i in range(0, 20, 2)],
            "mileage": [pygame.transform.scale(
                pygame.image.load("Image/enemy/lamp0.png"), (1, 1))],
        }

        # ✅ 左右車道：不固定車款，生成時隨機挑 enemy1-0 ~ enemy1-4
        # 不需要預先翻轉，讓 create() 處理

    @staticmethod
    def create(enemy_type, x, y, bullet_group):
        '''
        if enemy_type == "enemy1":
            # 隨機選一種 enemy1 變體
            variant = random.choice(EnemyFactory.enemy_variants)
            key = enemy_type + variant
            return Enemy(x, y,
                         animation=EnemyFactory.enemy_images[key],
                         bullet_group=bullet_group,
                         bullet_type=enemy_type,
                         value=100,
                         speedy_range=(2, 3))
        '''
        if enemy_type == "enemy_left":
            # ✅ 左車道：隨機選一種車款
            variant = random.choice(EnemyFactory.enemy_variants)
            key = "enemy1" + variant
            return Enemy(x, y,
                         animation=EnemyFactory.enemy_images[key],
                         bullet_group=bullet_group,
                         bullet_type=enemy_type,
                         value=150,
                         speedx_range=(0, 0),
                         speedy_range=(6, 8))   # 比較快

        elif enemy_type == "enemy_right":
            # ✅ 右車道：隨機選一種車款 + 翻轉
            variant = random.choice(EnemyFactory.enemy_variants)
            key = "enemy1" + variant
            flipped_images = [pygame.transform.flip(img, False, True) for img in EnemyFactory.enemy_images[key]]
            return Enemy(x, y,
                         animation=flipped_images,
                         bullet_group=bullet_group,
                         bullet_type=enemy_type,
                         value=150,
                         speedx_range=(0, 0),
                         speedy_range=(2, 4))   # 比較慢

        elif enemy_type == "police":
            return Enemy(x, y,
                         animation=EnemyFactory.enemy_images["police"],
                         bullet_group=bullet_group,
                         bullet_type=enemy_type,
                         value=100,
                         speedy_range=(2, 3))

        elif enemy_type == "enemy2":
            variant = random.choice(EnemyFactory.enemy_variants2)
            key = "enemy2" + variant
            return Enemy(x, y,
                         animation=EnemyFactory.enemy_images[key],
                         bullet_group=bullet_group,
                         bullet_type=enemy_type,
                         value=200,
                         speedy_range=(8, 9))

        elif enemy_type == "mileage":
            return Enemy(x, y,
                         animation=EnemyFactory.enemy_images["mileage"],
                         bullet_group=bullet_group,
                         bullet_type=enemy_type,
                         value=200,
                         speedx_range=(0, 0),
                         speedy_range=(10, 10))
