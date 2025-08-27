import pygame
import random
import Glo
from Config import *
from LevelConfig import LEVELS
from background import Background
from spaceship import Spaceship
from enemy_factory import EnemyFactory
from animation import Explosion, Heal
from progress import Progress
from boss import Boss1, Boss2, Boss3
from power import Power
from boss_enemy_factory import BossEnemyFactory

# 載入圖片資源
EnemyFactory.load_images(random.randint(0, 3))
BossEnemyFactory.load_images()



class GameModel:
    def __init__(self, user): 
        self.mile_ctr = 0
        self.user = user
        self.level = user.level
        self.config = LEVELS[user.level]

        self.background = Background(self.config["background"], 10 * Glo.SPEED_RATE)
        self.spaceship_group = pygame.sprite.GroupSingle(Spaceship())
        self.enemy_group = pygame.sprite.Group()
        self.enemy_bullet_group = pygame.sprite.Group()
        self.animation_group = pygame.sprite.Group()
        self.boss_group = pygame.sprite.GroupSingle()
        self.power_group = pygame.sprite.Group()
        
        self.mileage_group = pygame.sprite.Group()
        self.collide_delay = 1000
        self.last_collide_time = 0
        self.siren = pygame.mixer.Sound("Sound/police_siren.mp3")
       
        self.enemy_generator_time = 0
        self.enemy_generator_delay = random.randint(*self.config["enemy_delay"])

        self.run = False
        self.wait = False
        self.is_pass = False

        self.money = 0
        self.game_time = 0
        self.start_time = pygame.time.get_ticks()
        self.boss_time = self.config["boss_time"]
        self.progress = Progress(SCREEN_WIDTH - 50, 60, self.game_time, self.boss_time)
        self.power_probability = 0.8

        # Boss 小怪生成控制
        self.boss_enemy_time = 0
        self.boss_enemy_delay = 2000   # 每 2 秒生成一隻


    # ------------------ 更新邏輯 ------------------
    def update(self):
        self.check_for_state()
        self.background.update()
        self.spaceship_group.update()
        self.enemy_group.update()
        self.enemy_bullet_group.update()
        self.animation_group.update()
        self.boss_group.update()
        self.power_group.update()
        self.mileage_group.update()

        self.game_time = pygame.time.get_ticks() - self.start_time
        self.progress.update(self.game_time)
        Glo.TIMER = self.game_time

        self.enemy_generator()
        self.check_for_collisions()
        self.boss_appear()

        # ✅ Boss3 出現時，不斷生成小怪
        if self.level == 3 and self.boss_group:
            self.spawn_boss_enemies()


    def enemy_generator(self):
        now = pygame.time.get_ticks()
        if now - self.enemy_generator_time > self.enemy_generator_delay/(Glo.SPEED_RATE+0.05):

            # -----------------------
            # 車輛（馬路區）
            # -----------------------
            outer_margin = 150   # 避免壓到人行道
            inner_margin = 30    # 允許貼近中線

            # 左車道
            x_left = random.randint(outer_margin, SCREEN_WIDTH // 2 - inner_margin)
            enemy_left = EnemyFactory.create("enemy_left", x_left, 0, self.enemy_bullet_group)
            self.enemy_group.add(enemy_left)
            print(f"[Car] Left lane car at {x_left}")

            # 右車道
            x_right = random.randint(SCREEN_WIDTH // 2 + inner_margin, SCREEN_WIDTH - outer_margin)
            enemy_right = EnemyFactory.create("enemy_right", x_right, 0, self.enemy_bullet_group)
            self.enemy_group.add(enemy_right)
            print(f"[Car] Right lane car at {x_right}")

            # -----------------------
            # 行人（人行道區）
            # -----------------------
            pedestrian_margin = 60  # 行人距離遊戲視窗邊界的安全距離

            if random.random() < 0.5:  # 左人行道 (30% 機率)
                pedestrian_left = EnemyFactory.create(
                    "enemy2",
                    random.randint(pedestrian_margin, 120),  # ✅ 不會貼邊
                    0,
                    self.enemy_bullet_group
                )
                self.enemy_group.add(pedestrian_left)
                print("[Pedestrian] Spawned on LEFT sidewalk")

            if random.random() < 0.5:  # 右人行道 (30% 機率)
                pedestrian_right = EnemyFactory.create(
                    "enemy2",
                    random.randint(SCREEN_WIDTH - 120, SCREEN_WIDTH - pedestrian_margin),  # ✅ 不會貼邊
                    0,
                    self.enemy_bullet_group
                )
                self.enemy_group.add(pedestrian_right)
                print("[Pedestrian] Spawned on RIGHT sidewalk")

            # -----------------------
            # mileage (里程碑)
            # -----------------------
            enemy_type = "mileage"
            enemy = EnemyFactory.create(enemy_type, SCREEN_WIDTH-160, 0, self.enemy_bullet_group)
            self.mileage_group.add(enemy)

            # -----------------------
            # police (特殊敵人)
            # -----------------------
            if self.money > 1000 and random.randint(0, 2) > 1:
                self.siren.play()
                police_x = random.randint(outer_margin, SCREEN_WIDTH - outer_margin)
                enemy_police = EnemyFactory.create("police", police_x, 0, self.enemy_bullet_group)
                self.enemy_group.add(enemy_police)
                print(f"[Police] Spawned with siren at {police_x}")

            # 更新計時
            self.enemy_generator_time = now
            self.enemy_generator_delay = random.randint(*self.config["enemy_delay"])




    def check_for_collisions(self):
        ship = self.spaceship_group.sprite
        boss = self.boss_group.sprite

        # Spaceship 子彈
        for bullet in getattr(ship, "bullet_group", []):
            enemies_hit = pygame.sprite.spritecollide(bullet, self.enemy_group, True)
            for enemy in enemies_hit:
                self.money += enemy.value
                bullet.kill()
                self.animation_group.add(Explosion(enemy.rect.centerx, enemy.rect.centery, 100))
                if self.power_probability >= random.random():
                    self.power_group.add(Power(enemy.rect.centerx, enemy.rect.centery))

            bosses_hit = pygame.sprite.spritecollide(bullet, self.boss_group, False)
            for boss in bosses_hit:
                boss.hp -= bullet.damage
                bullet.kill()
                self.animation_group.add(
                    Explosion(boss.rect.centerx + random.randint(-60, 60),
                              boss.rect.centery + random.randint(-60, 60), 150)
                )

        # Enemy 與子彈
        for enemy in self.enemy_group.sprites():
            if pygame.sprite.spritecollide(enemy, self.spaceship_group, False):
                enemy.kill()
                ship.lives -= 1
                self.money += 0.5 * enemy.value
                Glo.SPEED_RATE = 0
                self.animation_group.add(Explosion(ship.rect.centerx, ship.rect.centery, 100))
                self.animation_group.add(Explosion(enemy.rect.centerx, enemy.rect.centery, 100))
            for bullet in enemy.bullet_group:
                if pygame.sprite.spritecollide(bullet, self.spaceship_group, False):
                    bullet.kill()
                    self.animation_group.add(Explosion(ship.rect.centerx, ship.rect.centery, 100))
                    ship.lives -= 1

        # Boss 子彈
        for bullet in getattr(self.boss_group.sprite, "bullet_group", []):
            if pygame.sprite.spritecollide(bullet, self.spaceship_group, False):
                bullet.kill()
                self.animation_group.add(Explosion(ship.rect.centerx, ship.rect.centery, 100))
                ship.lives -= 1

        # Boss 與玩家碰撞
        if pygame.sprite.spritecollide(self.spaceship_group.sprite, self.boss_group, False):
            now = pygame.time.get_ticks()
            if now - self.last_collide_time > self.collide_delay:
                boss.hp -= 10
                ship.lives -= 1
                self.money += 0.5 * boss.value if hasattr(boss, "value") else 0
                Glo.SPEED_RATE = 0
                self.animation_group.add(Explosion(ship.rect.centerx, ship.rect.centery, 100))
                self.animation_group.add(Explosion(boss.rect.centerx, boss.rect.centery, 100))
                self.last_collide_time = now


    def check_for_state(self):
        ship = self.spaceship_group.sprite
        if ship.lives <= 0:
            self.game_over()

        boss = self.boss_group.sprite
        if boss and boss.hp <= 0:
            self.money += boss.value
            boss.kill()
            #self.game_pass()
            ship.lives += 5
            
        for mileage in self.mileage_group.sprites():
            if mileage.rect.top > SCREEN_HEIGHT-80:
                mileage.kill()
                self.mile_ctr += 1
                print(self.mile_ctr)
                print(self.config["dest_mileage"])   
                if self.mile_ctr >= self.config["dest_mileage"]:
                    self.game_pass()
        

    def boss_appear(self):
        if self.game_time >= self.boss_time and not self.boss_group:
            boss_class = globals()[self.config["boss"]]
            self.boss_group.add(boss_class(SCREEN_WIDTH / 2, 0))
            print("Boss 出現了！")


    def spawn_boss_enemies(self):
        now = pygame.time.get_ticks()
        if now - self.boss_enemy_time > self.boss_enemy_delay:

            # 計算目前場上 boss 小怪數量
            current_boss_enemies = sum(
                1 for e in self.enemy_group
                if hasattr(e, "animation") and any(img in BossEnemyFactory.enemy_images.values() for img in [e.animation])
            )

            # ✅ 只要場上數量 < 上限，就補充生成
            if current_boss_enemies < BossEnemyFactory.max_enemies:
                num_enemies = random.randint(6, 10)  # 每次刷 3~6 隻
                num_enemies = min(num_enemies, BossEnemyFactory.max_enemies - current_boss_enemies)

                x_positions = [int(i * SCREEN_WIDTH / num_enemies) + 40 for i in range(num_enemies)]

                for x in x_positions:
                    enemy_type = random.choice(["boss3_1", "boss3_2", "boss3_3"])
                    enemy = BossEnemyFactory.create(enemy_type, x, -50, self.enemy_bullet_group, current_boss_enemies)

                    if enemy:
                        self.enemy_group.add(enemy)
                        current_boss_enemies += 1
                        print(f"[BossEnemy] 生成小怪: {enemy_type} at {x}")

            self.boss_enemy_time = now
            self.boss_enemy_delay = random.randint(800, 1500)  # 0.8 ~ 1.5 秒



    # ------------------ 控制方法 ------------------
    def reset(self):
        self.run = True
        self.wait = False
        self.is_pass = False
        self.spaceship_group.sprite.reset()
        self.enemy_group.empty()
        self.enemy_bullet_group.empty()
        self.boss_group.empty()
        self.animation_group.empty()
        self.power_group.empty()
        self.money = 0
        self.start_time = pygame.time.get_ticks()
        self.mileage_group.empty()
        self.mile_ctr = 0

    def game_over(self):
        self.run = False
        self.wait = True

    def game_pass(self):
        self.run = False
        self.wait = True
        self.is_pass = True
        self.user.level_up()

    def play_BGM(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Sound/bg_music.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
