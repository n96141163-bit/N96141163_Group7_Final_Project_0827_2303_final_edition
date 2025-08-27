# setting_bullet.py
from Config import *
import Glo


BULLET_CONFIG = {
    "spaceship": {
        "speedx": 0,
        "speedy": 14,
        "damage": 10, 
        "animation": True
    },
    "spaceship-double": {
        "speedx": 0,
        "speedy": 40,
        "damage": 8, 
        "animation": True
    }, 
    "spaceship-triple": {
        "speedx": 0,
        "speedy": 7,
        "damage": 4, 
        "animation": True
    },
    "enemy1": {
        "speedx": 0,
        "speedy": -4*Glo.SPEED_RATE,
        "damage": 1, 
        "animation": False
    },
    "police": {
        "speedx": 0,
        "speedy": -0.5*Glo.SPEED_RATE,
        "damage": 1, 
        "animation": False
    },
    "enemy2": {
        "speedx": 0,
        "speedy": -8*Glo.SPEED_RATE,
        "damage": 1, 
        "animation": False
    },
    "boss1": {
        "speedx": 0,
        "speedy": -10*Glo.SPEED_RATE,
        "damage": 1, 
        "animation": False
    }, 
    "boss2": {
        "speedx": 0,
        "speedy": -20*Glo.SPEED_RATE,
        "damage": 1, 
        "animation": False
    }, 
    "boss2-1": {
        "speedx": 0,
        "speedy": -4*Glo.SPEED_RATE,
        "damage": 1, 
        "animation": False
    }, 
    "boss3": {
        "speedx": 0,
        "speedy": -10*Glo.SPEED_RATE,
        "damage": 1, 
        "animation": False
    }, 
    "boss3-1": {
        "speedx": 0,
        "speedy": -10*Glo.SPEED_RATE,
        "damage": 1, 
        "animation": False
    }, 
}
