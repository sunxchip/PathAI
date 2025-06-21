# 자율주행 행동 예측 시스템

본 프로젝트는 자율주행 기능 구현을 위한 기존 ROS 기반 알고리즘 코드를 분석하여 머신러닝 기반 예측 시스템으로 확장하였습니다.

- `차선중심값계산.txt`, `장애물감지.txt`, `로봇제어.txt` 등의 코드를 참고하여  
  주요 입력 변수(center_offset, right_slope, 장애물 위치)와 판단 기준(정지/좌/우/직진)을 구성하였습니다.

- 이를 통해 센서 입력값만으로 행동을 예측하는 지도학습 기반 모델을 훈련하였으며,  
  결과는 PyGame 기반 시뮬레이터에서 시각적으로 표현하였습니다.
---

## 프로젝트 구조

- `sensor_data.csv` : 학습 및 테스트에 사용된 센서 데이터  
- `train_model.py` : 모델 학습 및 평가 코드 (RandomForestClassifier, SVM 비교 포함)  
- `predict_test.py` : 학습된 모델을 기반으로 테스트 시나리오 예측  
- `simulation.py` : PyGame을 활용한 예측 결과 시각화 시뮬레이션  

---

## 사용 모델
- Random Forest
- SVM (Support Vector Machine)

---

## 주요 성능 비교
- RandomForest: 높은 정밀도 및 feature importance 시각화 지원
- SVM: 일부 클래스에서 예측률 낮음

---

## 예측 가능한 행동
- 정지
- 좌회전
- 우회전
- 직진

---

## 시뮬레이션
PyGame을 활용하여 예측 결과에 따라 원이 방향을 바꾸며 움직이는 시뮬레이션 제공

---

## 환경
- Python 3.10
- scikit-learn
- pandas, numpy
- matplotlib, seaborn
- pygame

