import pandas as pd
from src.config import OUTPUTS_DIR
from src.data_loader import load_all_raw_data


def create_raw_tables_summary(dataframes: dict) -> pd.DataFrame:
    """
    Create a summary table showing row count, column count, and memory usage.
    """
    summary = []

    for table_name, df in dataframes.items():
        summary.append(
            {
                "table_name": table_name,
                "row_count": df.shape[0],
                "column_count": df.shape[1],
                "memory_usage_mb": round(df.memory_usage(deep=True).sum() / 1024**2, 2),
            }
        )

    return pd.DataFrame(summary)


def create_missing_values_summary(dataframes: dict) -> pd.DataFrame:
    """
    Create a summary table showing missing values for each column.
    """
    summary = []

    for table_name, df in dataframes.items():
        for column in df.columns:
            missing_count = df[column].isna().sum()
            missing_percentage = (missing_count / len(df)) * 100 if len(df) > 0 else 0

            summary.append(
                {
                    "table_name": table_name,
                    "column_name": column,
                    "missing_count": missing_count,
                    "missing_percentage": round(missing_percentage, 2),
                    "data_type": str(df[column].dtype),
                }
            )

    return pd.DataFrame(summary)


def create_duplicate_rows_summary(dataframes: dict) -> pd.DataFrame:
    """
    Create a summary table showing duplicate row counts for each table.
    """
    summary = []

    for table_name, df in dataframes.items():
        duplicate_count = df.duplicated().sum()
        duplicate_percentage = (duplicate_count / len(df)) * 100 if len(df) > 0 else 0

        summary.append(
            {
                "table_name": table_name,
                "duplicate_rows": duplicate_count,
                "duplicate_percentage": round(duplicate_percentage, 2),
            }
        )

    return pd.DataFrame(summary)


def save_data_quality_reports() -> None:
    """
    Load raw data, generate data quality reports, and save them to outputs folder.
    """
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

    dataframes = load_all_raw_data()

    raw_tables_summary = create_raw_tables_summary(dataframes)
    missing_values_summary = create_missing_values_summary(dataframes)
    duplicate_rows_summary = create_duplicate_rows_summary(dataframes)

    raw_tables_summary.to_csv(OUTPUTS_DIR / "raw_tables_summary.csv", index=False)
    missing_values_summary.to_csv(OUTPUTS_DIR / "missing_values_summary.csv", index=False)
    duplicate_rows_summary.to_csv(OUTPUTS_DIR / "duplicate_rows_summary.csv", index=False)

    print("Data quality reports generated successfully.")
    print(f"Saved to: {OUTPUTS_DIR}")


if __name__ == "__main__":
    save_data_quality_reports()