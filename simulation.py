import pygame
import joblib
import numpy as np

# pygame 초기화
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("로봇 행동 예측 시뮬레이션")
clock = pygame.time.Clock()

# 색상 정의
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
BLACK = (0, 0, 0)

# 로봇 초기 위치
x, y = 300, 200
radius = 15

# 모델 불러오기
model = joblib.load("behavior_model.pkl")

# 예제 센서 데이터
sensor_data = [
    [-35, 0.1, 0, 0, 1],   # 좌회전
    [0, 0.0, 0, 0, 0],     # 직진
    [20, 0.2, 1, 0, 0],    # 우회전
    [-10, 0.0, 0, 1, 0],   # 정지
    [15, -0.1, 0, 0, 1],   # 직진
]

# 움직임 함수
def move_robot(action):
    global x, y
    if action == 0:      # 정지
        pass
    elif action == 1:    # 좌회전
        x -= 2
    elif action == 2:    # 우회전
        x += 2
    elif action == 3:    # 직진
        y -= 2

# 메인 루프
running = True
index = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if index < len(sensor_data):
        input_data = np.array(sensor_data[index]).reshape(1, -1)
        prediction = model.predict(input_data)[0]
        print(f"[시나리오 {index+1}] 예측 행동: {['정지', '좌', '우', '직'][prediction]}")

        # 움직임을 부드럽게 10단계로 나눠서 실행
        steps = 10
        for _ in range(steps):
            screen.fill(WHITE)
            move_robot(prediction)
            pygame.draw.circle(screen, BLUE, (x, y), radius)
            pygame.display.flip()
            clock.tick(10)

        index += 1
    else:
        # 모든 시나리오 끝나면 1초간 보여주고 종료
        pygame.time.wait(1000)
        running = False

pygame.quit()
