import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

print("Loading dataset...")
df = pd.read_csv("data/student_data.csv")

print("Cleaning data...")
df.fillna(df.mean(), inplace=True)
# export processed data for dashboards or downstream use
os.makedirs("data", exist_ok=True)
df.to_csv("data/processed_student_data.csv", index=False)

X = df.drop(["Student_ID", "Final_GPA"], axis=1)
y = df["Final_GPA"]

print("Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training model...")
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
r2 = r2_score(y_test, predictions)
print("Model R2 Score:", r2)

import json

# ensure the output directory exists before trying to save the model and metadata
os.makedirs("models", exist_ok=True)
try:
    joblib.dump(model, "models/performance_model.pkl")
    # Save metadata for the dashboard (r2 and feature importances if available)
    metadata = {"r2": float(r2)}
    if hasattr(model, "feature_importances_"):
        feat = list(X.columns)
        metadata["feature_importances"] = dict(
            zip(feat, model.feature_importances_.tolist())
        )
    with open("models/metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    print("Model and metadata saved successfully in models/ folder")
except Exception as e:
    print(f"Error saving model or metadata: {e}")
    raise