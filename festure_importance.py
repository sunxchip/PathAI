# feature_importance.py

import joblib
import pandas as pd
import matplotlib.pyplot as plt

model = joblib.load("behavior_model.pkl")
df = pd.read_csv("sensor_data.csv")

X = df[['center_offset', 'right_slope', 'obsL', 'obsC', 'obsR']]
importances = model.feature_importances_
feature_names = X.columns

plt.figure(figsize=(8, 5))
plt.barh(feature_names, importances, color='skyblue')
plt.xlabel("Feature Importance")
plt.title("Random Forest - Feature Importance")
plt.grid(True)
plt.tight_layout()
plt.show()
