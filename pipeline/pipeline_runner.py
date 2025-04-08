import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from pipeline.load_data import load_raw_data
from pipeline.clean_transform import clean_and_engineer


PROCESSED_DATA_PATH = Path("data/processed/cleaned_FD001.csv")

def run_pipeline():
    df_raw = load_raw_data()
    df_clean = clean_and_engineer(df_raw)
    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"Processed data saved to {PROCESSED_DATA_PATH}")

if __name__ == "__main__":
    run_pipeline()
