import os
import sys
from datetime import datetime
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from collect.run_spider import run_spider


def extract_stock_number(stock_value: str) -> int:
    match = pd.Series(stock_value).str.extract(r"(\d+)")
    return match[0].fillna(0).astype(int)


def clean_price(df: pd.DataFrame) -> pd.DataFrame:
    df["price"] = df["price"].replace("[\$,]", "", regex=True).astype(float).fillna(0)
    return df


def clean_numerical_columns(df: pd.DataFrame) -> pd.DataFrame:
    df["average_rating"] = pd.to_numeric(df["average_rating"], errors="coerce").fillna(
        0
    )
    df["number_of_reviews"] = pd.to_numeric(
        df["number_of_reviews"], errors="coerce"
    ).fillna(0)
    return df


def transform_data() -> pd.DataFrame:

    data = run_spider()

    df = pd.DataFrame(data)
    df["date"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )  # Date format by ISO 8601 compatible with PostgreSQL

    df = clean_price(df)
    df = clean_numerical_columns(df)

    df["stock"] = df["stock"].apply(extract_stock_number)

    print(df)
    return df
