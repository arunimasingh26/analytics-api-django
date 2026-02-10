import pandas as pd

source = "sample_equipment_data.csv"

def validate_columns(df):
    EXPECTED_COLUMNS = {
        "Equipment Name",
        "Type",
        "Flowrate",
        "Pressure",
        "Temperature"
    }
    missing = EXPECTED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")


def read_csv(source):
    with open(source, "r") as f:
        df = pd.read_csv(f)
    if df.empty:
        raise ValueError("CSV file empty")
    validate_columns(df)
    return df

def compute_summary(df):
    return {
        "total_equipment": int(len(df)),
        "average_flowrate": float(df["Flowrate"].mean()),
        "average_pressure": float(df["Pressure"].mean()),
        "average_temperature": float(df["Temperature"].mean())
    }

def count_distribution(df):
    return {
        "count_by_type": df["Type"].value_counts().to_dict(),
        "average_flowrate_by_type": df.groupby("Type")["Flowrate"].mean().to_dict(),
        "average_pressure_by_type": df.groupby("Type")["Pressure"].mean().to_dict(),
        "average_temperature_by_type": df.groupby("Type")["Temperature"].mean().to_dict()
    }
   
def analyze_csv(source):
    df = read_csv(source)
    return {
        "summary": compute_summary(df),
        "count_distribution": count_distribution(df)
    }

