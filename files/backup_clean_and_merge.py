import pandas as pd
import glob
import os

def clean_and_merge():
    # Find all CSV files that match our naming pattern
    csv_files = glob.glob("site_*.csv")
    all_dfs = []

    for file in csv_files:
        df = pd.read_csv(file)
        
        # Standardize ID column
        id_cols = ['ParticipantID', 'id', 'ID']
        for col in id_cols:
            if col in df.columns:
                df = df.rename(columns={col: 'participant_id'})
        
        # Standardize Date column
        date_cols = ['Date', 'date_time', 'DATE']
        for col in date_cols:
            if col in df.columns:
                df = df.rename(columns={col: 'date'})
        
        # Standardize Score column (Site C used 'Value')
        if 'Value' in df.columns:
            df = df.rename(columns={'Value': 'score'})
        elif 'Score' in df.columns:
            df = df.rename(columns={'Score': 'score'})

        # Convert date to standard YYYY-MM-DD
        df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
        
        # Fill missing scores with the median of this site
        median_score = df['score'].median()
        df['score'] = df['score'].fillna(median_score)
        
        all_dfs.append(df)

    # Merge all dataframes
    master_df = pd.concat(all_dfs, ignore_index=True)
    
    # Save to master_dataset.csv
    master_df.to_csv('master_dataset.csv', index=False)
    print(f"Merged {len(csv_files)} files into 'master_dataset.csv'")

if __name__ == "__main__":
    clean_and_merge()
