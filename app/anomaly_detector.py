import pandas as pd

from app.data_loader import load_data


def detect_anomalies():

    df = load_data()

    resolution_time = df["resolution_time_hrs"].dropna()

    q1 = resolution_time.quantile(0.25)
    q3 = resolution_time.quantile(0.75)

    iqr = q3 - q1

    upper_limit = q3 + (1.5 * iqr)

    anomalies = df[
        df["resolution_time_hrs"] > upper_limit
    ]

    return anomalies


def detect_weekly_anomalies():

    df = load_data()

    df["created_at"] = pd.to_datetime(df["created_at"])

    latest_date = df["created_at"].max()

    week_start = latest_date - pd.Timedelta(days=7)

    df = df[
        (df["created_at"] >= week_start) &
        (df["created_at"] <= latest_date)
    ]

    resolution_time = df["resolution_time_hrs"].dropna()

    if resolution_time.empty:
        return df.iloc[0:0]

    q1 = resolution_time.quantile(0.25)
    q3 = resolution_time.quantile(0.75)

    iqr = q3 - q1

    upper_limit = q3 + (1.5 * iqr)

    anomalies = df[
        df["resolution_time_hrs"] > upper_limit
    ]

    return anomalies