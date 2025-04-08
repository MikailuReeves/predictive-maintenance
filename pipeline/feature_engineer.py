import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/processed/cleaned_FD001.csv")
OUTPUT_PATH = Path("data/processed/feature_engineered_FD001.csv")

def add_targets(df: pd.DataFrame) -> pd.DataFrame:
    # Add TTF: max cycle - current cycle per engine
    df['max_cycle'] = df.groupby('unit')['cycle'].transform('max')
    df['ttf'] = df['max_cycle'] - df['cycle'] # time to failure
    df.drop(columns=['max_cycle'], inplace=True)

    # will fail within 30 cycles
    df['label_30'] = (df['ttf'] <= 30).astype(int)

    return df

def run_feature_engineering():
    df = pd.read_csv(INPUT_PATH)
    df_fe = add_targets(df)
    df_fe.to_csv(OUTPUT_PATH, index=False)
    print(f"Feature-engineered dataset saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    run_feature_engineering()
