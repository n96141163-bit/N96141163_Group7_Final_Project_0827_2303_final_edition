# attack_strategy.py
import pygame
from bullet_factory import BulletFactory

BulletFactory.load_images()


class AttackStrategy:
    def __init__(self, duration=None):
        self.duration = duration  # 毫秒，None 代表永久
        self.start_time = None

    def activate(self):
        if self.duration:
            self.start_time = pygame.time.get_ticks()

    def is_expired(self):
        if self.duration is None:
            return False
        return pygame.time.get_ticks() - self.start_time >= self.duration

    def shoot(self, spaceship):
        raise NotImplementedError



class NormalAttack(AttackStrategy):
    def __init__(self):
        super().__init__(duration=None)  # 永久
    def shoot(self, spaceship):
        bullet = BulletFactory.create("spaceship", spaceship.rect.centerx, spaceship.rect.top)
        spaceship.bullet_group.add(bullet)
        spaceship.shoot_sound.play()


class DoubleAttack(AttackStrategy):
    def __init__(self):
        super().__init__(duration=3000)  # 3秒有效
    def shoot(self, spaceship):
        bullet1 = BulletFactory.create("spaceship-double", spaceship.rect.centerx - 7, spaceship.rect.top)
        bullet2 = BulletFactory.create("spaceship-double", spaceship.rect.centerx + 7, spaceship.rect.top)
        spaceship.bullet_group.add(bullet1, bullet2)
        spaceship.shoot_sound.play()


class TripleAttack(AttackStrategy):
    def __init__(self):
        super().__init__(duration=5000)  # 5秒有效
    def shoot(self, spaceship):
        bullet_center = BulletFactory.create("spaceship-triple", spaceship.rect.centerx, spaceship.rect.top, speedx_override=0)
        bullet_left = BulletFactory.create("spaceship-triple", spaceship.rect.centerx - 15, spaceship.rect.top, speedx_override=-1)
        bullet_right = BulletFactory.create("spaceship-triple", spaceship.rect.centerx + 15, spaceship.rect.top, speedx_override=1)
        spaceship.bullet_group.add(bullet_center, bullet_left, bullet_right)
        spaceship.shoot_sound.play()
