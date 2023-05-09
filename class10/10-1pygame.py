import pygame # 화면구성 및 이벤트 처리
import random # 랜덤 좌표값 생성

pygame.init()

# 변수에 저장해서 지속적인 화면 변화에 대응
# 가로, 세로 값은 추후 사용을 위해 변수로 저장
# 괄호를 두 번 사용하는 이유는 set_mode 함수의 매개변수가 배열 타입이기 때문
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("장애물 피하기 게임")

icon_width = 50
icon_height = 50

icon_color = (255,255,255)

# pygame.math.Vector2(x, y) = x, y 속성을 가지는 Vector2 타입
icon_position = pygame.math.Vector2(screen_width/2 - icon_width/2, screen_height/2 - icon_height/2)

icon_speed = pygame.math.Vector2(0, 0)

obstacle_width = 50
obstacle_height = 50
obstacle_color = (255, 255, 0) # 노란색
obstacle_count = 5 # 장애물 5개
obstacles = [] # 각 장애물의 위치를 담을 배열

for _ in range(obstacle_count):
    obstacles.append(pygame.math.Vector2(# 각 장애물의 위치를 배열에 추가
        random.randint(0, screen_width - obstacle_width), # 장애물 위치(x) 생성
        random.randint(-obstacle_height * 2, -obstacle_height))) # 장애물 위치(y) 생성

running = True
while running:
    screen.fill((0, 0, 0)) # 화면 색깔 채우기
    pygame.draw.rect(screen, icon_color, pygame.Rect(icon_position.x, icon_position.y,
                                                     icon_width, icon_height)) # 캐릭터 그리기
    for obs in obstacles:
        pygame.draw.rect(screen, obstacle_color, pygame.Rect(obs.x, obs.y, obstacle_width,
                                                             obstacle_height)) # 캐릭터 그리기
        pygame.display.flip() # 스크린 교체

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()

        icon_speed.x = 0.3 * (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
        icon_speed.y = 0.3 * (keys[pygame.K_DOWN] - keys[pygame.K_UP])

        icon_position += icon_speed

        icon_position.x = max(min(icon_position.x, screen_width - icon_width), 0)
        icon_position.y = max(min(icon_position.y, screen_height - icon_height), 0)

        for obs in obstacles:
            obs.y += 0.2

            if obs.y > screen_height:
                obs.x = random.randint(0, screen_width - obstacle_width)
                obs.y = random.randint(-obstacle_width * 2, -obstacle_width)
        
        icon_rect = pygame.Rect(icon_position.x, icon_position.y, icon_width, icon_height)
            
        for obs in obstacles:
            obstacle_rect = pygame.Rect(obs.x, obs.y, obstacle_width, obstacle_height)
                
            if icon_rect.colliderect(obstacle_rect):
                print("게임 오버")
                running = False

pygame.quit()