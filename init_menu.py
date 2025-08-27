import pygame
from Config import *



class InitMenu:
    def __init__(self, user):
        self.run = True
        self.image = pygame.image.load("Image/init_menu.png")
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        '''
        self.image = pygame.image.load("Image/menu_add0.png")
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH-300, SCREEN_HEIGHT-400))
        '''
        self.user = user

    def draw(self, surface):
                
        # (1)---畫出初起畫面有的文字、圖片---
        surface.blit(self.image,(0,0))
        self.draw_text(surface,"瘋 狂 外 送", 100, RED, True, SCREEN_WIDTH/2, 220)
        self.draw_text(surface,"選 擇 關 卡", 36, WHITE, True, SCREEN_WIDTH/2, 350)

        # 三個關卡選擇
        self.draw_text(surface,"按 1 進 入 關 卡 一", 28, WHITE, False, SCREEN_WIDTH/2, 650)
        self.draw_text(surface,"按 2 進 入 關 卡 二", 28, WHITE, False, SCREEN_WIDTH/2, 700)
        self.draw_text(surface,"按 3 進 入 關 卡 三", 28, WHITE, False, SCREEN_WIDTH/2, 750)

        self.draw_text(surface,"按 P 開 始 送 餐", 28, BLACK, True, SCREEN_WIDTH/2, 400)
        self.draw_text(surface,"按 住 I 查 看 說 明", 28, BLACK, True, SCREEN_WIDTH/2, 450)
        self.draw_text(surface,f"- 訂 單 {self.user.level} -", 28, WHITE, True, SCREEN_WIDTH/2, 560) 
        self.draw_text(surface, f"預 估 交 保 金 額 : {self.user.money}萬", 24, WHITE, True, 160, 50)
        #self.draw_text(surface, f"{str(s).zfill(5)}", 24, WHITE, False, 50, 35)
        #surface.blit(pygame.transform.scale(pygame.image.load(f"Image/level{self.user.level}.jpg"),(SCREEN_WIDTH, SCREEN_HEIGHT)))
        #surface.blit(pygame.transform.scale(pygame.image.load(f"Image/level{self.user.level}.jpg"), (300,150)),(325-150,600))
        keys = pygame.key.get_pressed()              #new add 
        if keys[pygame.K_i]:
            pygame.draw.rect(surface, WHITE, (0, 0, 650, 800), 0)
            self.draw_text(surface, f"《 遊 戲 介 紹 》", 36, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-350)
            self.draw_text(surface, f"你 是 一 名 暴 躁 的 外 送 員, 在 台 南 這", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-300)
            self.draw_text(surface, f"個 交 通 險 惡 的 地 方 接 到 外 送 訂 單 ", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-270)
            self.draw_text(surface, f"請 克 服 (或 擊 敗 ) 蛇 行 車 輛 以 及 強 ", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-240)
            self.draw_text(surface, f"大 的 馬 路 三 寶 來 完 成 外 送 任 務 ！", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-210)
            self.draw_text(surface, f"盡 力 在 越 短 的 時 間 內 完 成 外 送 所 ", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-180)
            self.draw_text(surface, f"需 路 程", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-150)
            
            self.draw_text(surface, f"《 遊 戲 設 定 》", 36, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-100)
            self.draw_text(surface, f"鍵 盤 WASD：上 下 左 右 移 動", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-50)
            self.draw_text(surface, f"鍵 盤 空 白 鍵：射 擊 ( 丟 便 當 )", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2-20)
            self.draw_text(surface, f"鍵 盤 E/Q：加 速 / 減 速", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2+10)
            self.draw_text(surface, f"撞 擊 車 輛 或 路 人 : 生 命 值↓ 交 保 金 額↑", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2+40)
            self.draw_text(surface, f"射 殺 車 輛 或 路 人 : 交 保 金 額↑↑", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2+70)
            self.draw_text(surface, f"射 殺 三 寶 BOSS : 交 保 金 額↑  生 命 值↑", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2+100)
            self.draw_text(surface, f"《 遊 戲 結 果 》", 36, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2+150)
            self.draw_text(surface, f" 1. 顧 客 滿 意 度 ", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2+200)
            self.draw_text(surface, f" 2. 是 否 守 法 ", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2+230)
            self.draw_text(surface, f" 3. 是 否 能 夠 保 釋 ", 28, BLACK, False, SCREEN_WIDTH/2, SCREEN_HEIGHT/2+260)
             
            
             
            
                
            

        pass

    def draw_text(self, surface, text, size, color, bold, x, y):
        font = pygame.font.Font("Font/BoutiqueBitmap9x9_Bold_1.9.ttf", size=size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.centerx = x
        text_rect.top = y
        surface.blit(text_surface, text_rect)