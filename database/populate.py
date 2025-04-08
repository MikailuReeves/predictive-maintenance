import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("data/engine_data.db")
CSV_PATH = Path("data/processed/feature_engineered_FD001.csv")

def insert_data():
    df = pd.read_csv(CSV_PATH)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open("database/schema.sql", "r") as f:
        cursor.executescript(f.read())

    df.to_sql("engine_cycles", conn, if_exists="append", index=False)
    conn.commit()
    conn.close()
    print(f"Inserted {len(df)} rows into engine_cycles.")

if __name__ == "__main__":
    insert_data()
