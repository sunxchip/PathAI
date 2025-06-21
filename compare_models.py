import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# 데이터 불러오기
df = pd.read_csv("sensor_data.csv")
X = df[['center_offset', 'right_slope', 'obsL', 'obsC', 'obsR']]
y = df['label']

# 학습/검증 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest 모델
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
print("===== Random Forest 결과 =====")
print(classification_report(y_test, y_pred_rf))

# SVM 모델
svm_model = SVC(kernel='rbf')  # 기본 RBF 커널 사용
svm_model.fit(X_train, y_train)
y_pred_svm = svm_model.predict(X_test)
print("===== SVM 결과 =====")
print(classification_report(y_test, y_pred_svm))
