import pandas as pd
import glob
import os

# Find all CSV files in the current folder
csv_files = glob.glob("site_*.csv")

for file in csv_files:
    print(f"\n--- Filename: {file} ---")
    df = pd.read_csv(file)
    print("Columns:", list(df.columns))
    print("Missing values per column:")
    print(df.isnull().sum())
