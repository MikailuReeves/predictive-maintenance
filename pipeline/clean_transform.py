import pandas as pd

def clean_and_engineer(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = ['unit', 'cycle'] + [f'op_setting_{i}' for i in range(1, 4)] + [f'sensor_{i}' for i in range(1, 22)]

    # Calculate time-to-failure (TTF)
    df['max_cycle'] = df.groupby('unit')['cycle'].transform('max')
    df['ttf'] = df['max_cycle'] - df['cycle']

    df.drop(columns=['max_cycle'], inplace=True)

    # rolling average of sensor_2 over 5 cycles
    df['sensor_2_rolling'] = df.groupby('unit')['sensor_2'].rolling(window=5, min_periods=1).mean().reset_index(0, drop=True)

    return df
