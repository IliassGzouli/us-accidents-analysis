import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print(f"Données chargées : {df.shape[0]} lignes, {df.shape[1]} colonnes")
    return df

def save_clean_data(df, path):
    df.to_csv(path, index=False)
    print(f"Données sauvegardées dans : {path}")