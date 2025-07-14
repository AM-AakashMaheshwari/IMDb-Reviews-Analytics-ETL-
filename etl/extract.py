import pandas as pd


def extract_csv(path, drop_index=True):
    df = pd.read_csv(path)
    if drop_index and 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    return df

def clean_columns(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df
