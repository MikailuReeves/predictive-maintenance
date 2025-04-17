import pandas as pd

def get_last_cycle_per_unit(df: pd.DataFrame, unit_col: str = "unit", cycle_col: str = "cycle") -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): _description_ DataFrame containing unit and cycle columns.
        unit_col (str, optional): _description_. The name of the column representing engine unit IDs. Defaults to "unit".
        cycle_col (str, optional): _description_. The name of the column representing time cycles. Defaults to "cycle".

    Returns:
        pd.DataFrame: DataFrame with the last cycle for each unit.
    """
    idx = df.groupby(unit_col)[cycle_col].idxmax()
    return df.loc[idx].reset_index(drop=True)
