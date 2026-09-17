import pandas as pd
from app.data_loader import load_data

def unresolved_high_priority_tickets(hours):
    df = load_data()

    df["created_at"] = pd.to_datetime(df["created_at"])

    current_time = df["created_at"].max()

    df["hours_open"] = (
        current_time - df["created_at"]
    ).dt.total_seconds() / 3600

    result = df[
        (df["priority"].isin(["High", "Critical"])) &
        (df["status"] != "Resolved") &
        (df["hours_open"] > hours)
    ]

    result = result.drop(columns=["hours_open"])

    result = result.astype(object).where(
        pd.notna(result),
        None
    )

    return result

def count_tickets():
    df = load_data()
    return len(df)


def count_by_status():
    df = load_data()
    return df["status"].value_counts()


def filter_tickets(column, value):
    df = load_data()
    result = df[df[column] == value]
    return result


def filter_multiple(column1, value1, column2, value2):
    df = load_data()

    result = df[
        (df[column1] == value1) &
        (df[column2] == value2)
    ]

    return result


def average_response_time():
    df = load_data()
    return df["response_time_hrs"].mean()


def average_resolution_time():
    df = load_data()
    return df["resolution_time_hrs"].mean()


def count_by_category():
    df = load_data()
    return df["category"].value_counts()


def count_by_priority():
    df = load_data()
    return df["priority"].value_counts()


def count_by_status_value(status):
    df = load_data()
    return len(df[df["status"] == status])


def most_resolved_agent(period=None):
    df = load_data()

    df["created_at"] = pd.to_datetime(df["created_at"])

    if period == "latest_month":

        latest_date = df["created_at"].max()

        df = df[
            (df["created_at"].dt.year == latest_date.year) &
            (df["created_at"].dt.month == latest_date.month)
        ]

    resolved = df[df["status"] == "Resolved"]

    result = resolved["agent_id"].value_counts()

    if result.empty:
        return "No resolved tickets found."

    return result.idxmax()


def average_customer_rating(category):
    df = load_data()

    result = df[
        df["category"] == category
    ]["customer_rating"].mean()

    return result


def filter_by_conditions(priority, status, resolution_time):
    df = load_data()

    df["created_at"] = pd.to_datetime(df["created_at"])

    current_time = df["created_at"].max()

    df["hours_open"] = (
        current_time - df["created_at"]
    ).dt.total_seconds() / 3600

    result = df[
        (df["priority"] == priority) &
        (
            (
                (df["status"] != status) &
                (df["hours_open"] > resolution_time)
            )
            |
            (
                (df["status"] == status) &
                (df["resolution_time_hrs"] > resolution_time)
            )
        )
    ]

    result = result.astype(object).where(pd.notna(result), None)

    return result


def count_critical_unresolved():
    df = load_data()

    result = df[
        (df["priority"] == "Critical") &
        (df["status"] != "Resolved")
    ]

    return len(result)

def lowest_agent_rating():
    df = load_data()

    ratings = (
        df.dropna(subset=["customer_rating"])
        .groupby("agent_id")["customer_rating"]
        .mean()
    )

    if ratings.empty:
        return "No customer ratings found."

    return ratings.idxmin()


def execute_query(query):

    df = load_data()

    action = query["action"]

    if action == "count":

        column = query.get("column")
        value = query.get("value")

        if column == "ticket_id" and value == "":
            return len(df)

        result = df[df[column] == value]

        return len(result)

    elif action == "lowest_agent_rating":
        return lowest_agent_rating()

    elif action == "critical_unresolved":
        return count_critical_unresolved()

    elif action == "average":

        column = query.get("column")

        result = df[column].mean()

        return result

    elif action == "most_resolved_agent":

        period = query.get("period")

        return most_resolved_agent(period)

    elif action == "average_rating":

        category = query.get("category")

        return average_customer_rating(category)

    elif action == "filter":

        priority = query.get("priority")
        status = query.get("status")
        resolution_time = query.get("resolution_time")

        result = filter_by_conditions(
            priority,
            status,
            resolution_time
        )

        return result.to_dict(orient="records")

    elif action == "weekly_anomalies":
        from app.anomaly_detector import detect_weekly_anomalies

        result = detect_weekly_anomalies()

        result = result.astype(object).where(pd.notna(result), None)

        return result.to_dict(orient="records")

    elif action == "unresolved_high_priority":
        hours = query.get("hours", 24)

        result = unresolved_high_priority_tickets(hours)

        return result.to_dict(orient="records")

    elif action == "unknown":

        return "I can only answer questions about the support tickets."

    return "Unsupported query"