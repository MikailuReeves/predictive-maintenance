import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path("model/artifacts/rf_classifier.pkl")

def load_model():
    return joblib.load(MODEL_PATH)

def preprocess_raw_file(txt_path: str) -> pd.DataFrame: 
    """
    Converts a raw NASA test .txt file into a model-ready DataFrame.
    Adds headers and rolling average features.
    """
    df = pd.read_csv(txt_path, sep="\s+", header=None)
    df.dropna(axis=1, how='all', inplace=True)
    df.columns = ['unit', 'cycle'] + \
                 [f'op_setting_{i}' for i in range(1, 4)] + \
                 [f'sensor_{i}' for i in range(1, 22)]

    # Add rolling feature used during training
    df['sensor_2_rolling'] = df.groupby('unit')['sensor_2'].rolling(window=5, min_periods=1).mean().reset_index(0, drop=True)

    return df

def predict_from_csv(csv_path: str, output_path: str = None, is_raw: bool = False):
    """
    Predict failure risk from a CSV or raw .txt file.
    If is_raw=True, will preprocess the input to match model training format.
    """
    model = load_model()
    
    if is_raw:
        df = preprocess_raw_file(csv_path)
    else:
        df = pd.read_csv(csv_path)

    # Drop non-feature columns
    drop_cols = ['unit', 'cycle', 'ttf', 'label_30']
    df_features = df.drop(columns=[col for col in drop_cols if col in df.columns], errors='ignore')

    # Predict
    df['predicted_label'] = model.predict(df_features)
    df['prob_class_1'] = model.predict_proba(df_features)[:, 1]
    df['risk_level'] = df['prob_class_1'].apply(lambda p: "High" if p > 0.8 else "Medium" if p > 0.5 else "Low")

    if output_path:
        df.to_csv(output_path, index=False)
        print(f"Predictions saved to {output_path}")
    else:
        print(df[['predicted_label', 'prob_class_1', 'risk_level']].head())

    return df
