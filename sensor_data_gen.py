import csv
import random

# 파일 생성
with open("sensor_data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['center_offset', 'right_slope', 'obsL', 'obsC', 'obsR', 'label'])

    for _ in range(500):  # 500개의 샘플
        offset = random.uniform(-40, 40)  # 차선 중심 오프셋
        slope = random.uniform(-0.3, 0.3)  # 우측 차선 기울기
        obsL = random.choice([0, 1])
        obsC = random.choice([0, 1])
        obsR = random.choice([0, 1])

        # 행동 라벨 (룰 기반)
        if obsC:
            label = 0  # 정지
        elif offset < -15:
            label = 1  # 좌회전
        elif offset > 15:
            label = 2  # 우회전
        else:
            label = 3  # 직진

        writer.writerow([offset, slope, obsL, obsC, obsR, label])
