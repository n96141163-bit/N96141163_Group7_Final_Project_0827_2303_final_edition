import pygame
from Config import *
import Glo
from LevelConfig import LEVELS
from game_model import GameModel
import time


class GameView:
    def __init__(self, user):       #整個init為新增
        self.user = user
        self.level = user.level
        self.config = LEVELS[user.level]
        self.ambu = pygame.mixer.Sound("Sound/ambulance.mp3")
        self.ambu.set_volume(0.3)
        self.vict = pygame.mixer.Sound("Sound/victory.mp3")
        self.vict.set_volume(0.3)
        self.ambuStop = 0
    def draw(self, model, surface):
        model.background.draw(surface)
        model.spaceship_group.draw(surface)
        model.spaceship_group.sprite.bullet_group.draw(surface)
        model.enemy_group.draw(surface)
        model.enemy_bullet_group.draw(surface)
        model.animation_group.draw(surface)
        model.boss_group.draw(surface)
        #model.power_group.draw(surface)
        model.progress.draw(surface)
        model.mileage_group.draw(surface)          #新增
        
        #self.config = LEVELS[user.level]            #新增

        # Boss HP
        if model.boss_group:
            model.boss_group.sprite.draw_hp(surface)
            model.boss_group.sprite.bullet_group.draw(surface)
            
        #遊戲中畫面會出現的 str(model.money).zfill(5)   Glo.SPEED_RATE*50} self.config["dest_mileage"]
        self.draw_text(surface, f"訂 單 {model.user.level}", 20, WHITE, False, SCREEN_WIDTH-65, 17)
        
        self.draw_text(surface, f"  剩 餘 距 離 {int(self.config["dest_mileage"] - model.mile_ctr)} ", 20, WHITE, False, 100, SCREEN_HEIGHT-170)
        self.config = LEVELS[model.user.level]
        #self.draw_text(surface, f"{int(self.config["dest_mileage"] - model.mile_ctr)} ", 20, WHITE, False, 100, SCREEN_HEIGHT-150)
        
        self.draw_text(surface, f"  花 費 時 間 {int(Glo.TIMER/1000)} 秒", 20, WHITE, False, 100, SCREEN_HEIGHT-130)
        #self.draw_text(surface, f"{int(Glo.TIMER/1000)} 秒", 20, WHITE, False, 100, SCREEN_HEIGHT-110)
        
        self.draw_text(surface, f"    油 門 時 速 {int(Glo.SPEED_RATE*50)} km/hr ", 20, WHITE, False, 100, SCREEN_HEIGHT-90)
        #self.draw_text(surface, f"{int(Glo.SPEED_RATE*50)} km/hr", 20, WHITE, False, 100, SCREEN_HEIGHT-70)
 
        self.draw_text(surface, f"    預 估 交 保 金 額 {model.money}萬 ", 20, WHITE, False, 100, SCREEN_HEIGHT-50)
        #self.draw_text(surface, f"{model.money}萬", 20, WHITE, False, 100, SCREEN_HEIGHT-30)
        
        self.draw_text(surface, "生 命 值", 20, WHITE, False, 55, 17)
        for i in range(model.spaceship_group.sprite.lives):
            surface.blit(LIVES_ICON, (i*40+90, 10))

        # Text & Money & Lives
        if not model.run:
            if model.is_pass:
                
                keys = pygame.key.get_pressed()
                pygame.draw.rect(surface, WHITE, (0, 0, 650, 800), 0)
                surface.blit(pygame.transform.scale(pygame.image.load("Image/complete.png"),(325, 400)), (162.5, 400))
                self.draw_text(surface, "按 住 B 看 一 項 結 果", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-350)
                self.draw_text(surface, "按 住 N 看 一 項 結 果", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-300)
                self.draw_text(surface, "按 住 M 看 一 項 結 果", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-250)
                self.draw_text(surface, "：「您 的 餐 點 到 囉 !」", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-200)
                self.draw_text(surface, ":「謝 謝, 慢 走！ 」", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-150)
                self.draw_text(surface, "按 R 接 下 個 訂 單", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-100)
                
                if keys[pygame.K_b]:
                    pygame.draw.rect(surface, WHITE, (0, 0, 650, 800), 0)
                    if Glo.TIMER/1000 <= 30:
                        surface.blit(pygame.transform.scale(pygame.image.load("Image/feedback5.png"),(250, 400)), (200, 400))
                        self.draw_text(surface, f"《 5 星 好 評 (花{int(Glo.TIMER/1000)}秒, <= 30 秒)》", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-250)
                        self.draw_text(surface, "：「今 天 的 餐 好 像 特 別 早 到? 」", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-200)
                        #self.draw_text(surface, ":「好, 抱 歉。 沒 其 他 罪 了 吧?」", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-150)
                        self.vict.play()
                    else:
                        surface.blit(pygame.transform.scale(pygame.image.load("Image/feedback3.png"),(250, 400)), (200, 400))
                        
                        self.draw_text(surface, f"《 沒 有 5 星  (花{int(Glo.TIMER/1000)}秒, > 30 秒)》", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-250)
                        self.draw_text(surface, "：「...」", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-200)
                        
                        pass
                
                if keys[pygame.K_n]:
                    pygame.draw.rect(surface, WHITE, (0, 0, 650, 800), 0)
                    if Glo.EXCEEDSPEED == True:
                        surface.blit(pygame.transform.scale(pygame.image.load("Image/punish.png"),(325, 400)), (162.5, 400))
                        self.draw_text(surface, "《 超 速 (速 限 100)》", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-250)
                        self.draw_text(surface, "：「你 騎 到 超 過 100,  請 留 意 」", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-200)
                        self.draw_text(surface, ":「好, 抱 歉。 沒 其 他 罪 了 吧?」", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-150)
                    else:
                        surface.blit(pygame.transform.scale(pygame.image.load("Image/leo.png"),(325, 400)), (162.5, 400))
                        self.draw_text(surface, "《 車 速 合 法 》", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-250)
                        self.draw_text(surface, "：「我 是 守 速 限 的 好 公 民」", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-200)
                        self.draw_text(surface, ":「省省吧 叫 food*anda 送！」", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-150)
                if keys[pygame.K_m]:
                    pygame.draw.rect(surface, WHITE, (0, 0, 650, 800), 0)
                    if model.money > 1500:
                        surface.blit(pygame.transform.scale(pygame.image.load("Image/prison.png"),(325, 400)), (162.5, 400))
                        self.draw_text(surface, f"《 我 付 不 出 交 保 金 ({int(model.money)}萬)》", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-250)
                        self.draw_text(surface, "：「你 好, 我 沒 亂 騎 車, 現 在 被 關", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-200)
                        self.draw_text(surface, f"還 差 {int(model.money-1500)}萬 能 交 保, 我 的 支 付", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-150)
                        self.draw_text(surface, "寶 號 碼 是...我 承 諾 幫 你 外 送...", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-100)
                    else:
                        surface.blit(pygame.transform.scale(pygame.image.load("Image/iAmRich.png"),(325, 400)), (162.5, 400))
                        self.draw_text(surface, "《 外 送 只 是 做 興 趣 的 》", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-250)
                        self.draw_text(surface, f"：「{(int(model.money))}萬 交 保? 沒 問 題」", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-200)
                        
            else:
                pygame.draw.rect(surface, WHITE, (0, 0, 650, 800), 0)
                surface.blit(pygame.transform.scale(pygame.image.load("Image/iNeedHelp.png"),(325, 400)), (162.5, 400))
                self.draw_text(surface, ":「你 也 是 78 歲 ?」", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-200)
                self.draw_text(surface, ":「$ % # @ < X ...」", 36, RED, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-150)
                self.draw_text(surface, "按 R : 這 局 重 來", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-100)
               
                self.ambu.play()
                    
                
            self.draw_text(surface, "按 Q 回 主 頁 面", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-50)
        
        

    def draw_text(self, surface, text, size, color, bold, x, y):
        font = pygame.font.Font("Font/BoutiqueBitmap9x9_Bold_1.9.ttf", size=size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.centerx = x
        text_rect.top = y
        surface.blit(text_surface, text_rect)
