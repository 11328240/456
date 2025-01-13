import pygame
import random
import sys

# 初始化 pygame
pygame.init()

# 屏幕設置
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("小恐龍遊戲")

# 顏色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)

# 小恐龍參數
dino_width = 50
dino_height = 50
dino_x = 50
dino_y = screen_height - dino_height - 10
dino_velocity = 10
is_jumping = False
jump_height = 15
fall_speed = 0

# 障礙物參數
obstacle_width = 30
obstacle_height = 50
obstacle_velocity = 7
obstacles = []

# 遊戲時鐘
clock = pygame.time.Clock()

def draw_dino():
    pygame.draw.rect(screen, GREEN, (dino_x, dino_y, dino_width, dino_height))

def draw_obstacles():
    for obs in obstacles:
        pygame.draw.rect(screen, BROWN, obs)

def main():
    global dino_y, is_jumping, fall_speed, obstacles

    score = 0
    while True:
        screen.fill(WHITE)

        # 檢查事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 處理小恐龍跳躍
        keys = pygame.key.get_pressed()
        if not is_jumping:
            if keys[pygame.K_SPACE]:
                is_jumping = True
                fall_speed = -jump_height
        else:
            dino_y += fall_speed
            fall_speed += 1
            if dino_y >= screen_height - dino_height - 10:
                dino_y = screen_height - dino_height - 10
                is_jumping = False

        # 障礙物移動
        if random.randint(1, 100) < 3:
            obstacle_x = screen_width
            obstacle_y = screen_height - obstacle_height - 10
            obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

        for obs in obstacles[:]:
            obs.x -= obstacle_velocity
            if obs.x + obstacle_width < 0:
                obstacles.remove(obs)
                score += 1
            if obs.colliderect(pygame.Rect(dino_x, dino_y, dino_width, dino_height)):
                pygame.quit()
                sys.exit()

        # 畫出小恐龍和障礙物
        draw_dino()
        draw_obstacles()

        # 顯示分數
        font = pygame.font.SysFont("Arial", 30)
        score_text = font.render(f"分數: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
