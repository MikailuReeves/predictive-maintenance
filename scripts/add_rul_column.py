import pandas as pd

def add_rul_column(df: pd.DataFrame, unit_col: str = "unit", cycle_col: str = "cycle") -> pd.DataFrame:
    """
    Adds a 'rul' column to the dataframe representing Remaining Useful Life at each cycle.
    
    Parameters:
    - df: DataFrame containing unit and cycle columns.
    - unit_col: name of the column representing engine unit IDs.
    - cycle_col: name of the column representing time cycles.
    
    Returns:
    - DataFrame with an added 'rul' column.
    """
    max_cycles = df.groupby(unit_col)[cycle_col].transform("max")
    df["rul"] = max_cycles - df[cycle_col]
    return df
