from pathlib import Path
import pandas as pd

RAW_DATA_PATH = Path("data/raw/train_FD001.txt")

def load_raw_data():
    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(f"Raw dataset not found at {RAW_DATA_PATH}")
    df = pd.read_csv(RAW_DATA_PATH, sep=' ', header=None)
    df.dropna(axis=1, how='all', inplace=True)  # Drop empty columns (NASA format quirk)
    return df
