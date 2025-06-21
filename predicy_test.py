import joblib

# 저장된 모델 불러오기
model = joblib.load("behavior_model.pkl")

# 행동 라벨 정의
actions = {
    0: "정지",
    1: "좌회전",
    2: "우회전",
    3: "직진"
}

#  시나리오 입력값들: [center_offset, right_slope, obsL, obsC, obsR]
scenarios = [
    [-35,  0.1, 0, 0, 1],   # 왼쪽 치우침 + 우측 장애물 → 좌회전?
    [   0,  0.0, 0, 0, 0],   # 완전 중앙 + 장애물 없음 → 직진?
    [  20,  0.2, 1, 0, 0],   # 오른쪽 치우침 + 좌측 장애물 → 우회전?
    [ -10,  0.0, 0, 1, 0],   # 정면 장애물 있음 → 정지?
    [  15, -0.1, 0, 0, 1],   # 오른쪽 경사 + 오른쪽 장애물 → 좌회전?
    [ -20, -0.2, 1, 0, 1],   # 양쪽 장애물 + 왼쪽 치우침 → 좌회전?
]

# 결과 출력
print(" 예측 테스트 시나리오 결과")
for i, s in enumerate(scenarios, 1):
    pred = model.predict([s])[0]
    print(f"[시나리오 {i}] 센서입력: {s} → 예측 행동: {actions[pred]}")
