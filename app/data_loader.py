import pandas as pd

def load_data():
    file_path = "data/support_tickets.csv"

    df = pd.read_csv(file_path)
    return df
