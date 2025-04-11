import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path("model/artifacts/rf_classifier.pkl")

def load_model():
    return joblib.load(MODEL_PATH)

def predict_risk(sensor_data: dict) -> dict:
    """
    sensor_data: dict of input features (must match training column names exactly)
    returns: dict with class prediction and probability
    """
    model = load_model()
    
    # Convert input to DataFrame
    X_input = pd.DataFrame([sensor_data])

    # Predict class and probability
    prediction = model.predict(X_input)[0]
    proba = model.predict_proba(X_input)[0][1]  # probability of class 1

    return {
        "predicted_label": int(prediction),
        "probability_class_1": round(proba, 4),
        "risk_level": "High" if proba > 0.8 else "Medium" if proba > 0.5 else "Low"
    }
