
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import matplotlib
matplotlib.rcParams['font.family'] = 'AppleGothic'  # Mac 기본 한글 폰트
matplotlib.rcParams['axes.unicode_minus'] = False   # 마이너스 기호 깨짐 방지
import seaborn as sns
import matplotlib.pyplot as plt

# CSV 불러오기
df = pd.read_csv("sensor_data.csv")

X = df[['center_offset', 'right_slope', 'obsL', 'obsC', 'obsR']]
y = df['label']

# 훈련/테스트 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 학습
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 성능 평가 출력
print("분류 성능:\n")
print(classification_report(y_test, y_pred))

# confusion matrix 시각화
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, cmap="Blues", fmt="d",
            xticklabels=["정지", "좌", "우", "직"],
            yticklabels=["정지", "좌", "우", "직"])
plt.xlabel("예측값")
plt.ylabel("실제값")
plt.title("Confusion Matrix")
plt.show()

# 모델 저장
joblib.dump(model, "behavior_model.pkl")
print("모델 저장 완료: behavior_model.pkl")
