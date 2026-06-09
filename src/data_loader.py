import pandas as pd
from pathlib import Path
from src.config import RAW_DATA_DIR, EXPECTED_RAW_FILES


def validate_raw_files(raw_data_dir: Path = RAW_DATA_DIR) -> None:
    """
    Validate that all expected raw CSV files exist in the raw data directory.
    """
    missing_files = []

    for file_name in EXPECTED_RAW_FILES:
        file_path = raw_data_dir / file_name

        if not file_path.exists():
            missing_files.append(file_name)

    if missing_files:
        missing_files_text = "\n".join(missing_files)
        raise FileNotFoundError(
            f"The following raw files are missing:\n{missing_files_text}"
        )

    print("All expected raw CSV files are available.")


def load_csv(file_name: str, raw_data_dir: Path = RAW_DATA_DIR) -> pd.DataFrame:
    """
    Load a single CSV file from the raw data directory.
    """
    file_path = raw_data_dir / file_name
    return pd.read_csv(file_path)


def load_all_raw_data(raw_data_dir: Path = RAW_DATA_DIR) -> dict:
    """
    Load all expected raw CSV files into a dictionary of DataFrames.
    """
    validate_raw_files(raw_data_dir)

    dataframes = {}

    for file_name in EXPECTED_RAW_FILES:
        table_name = file_name.replace(".csv", "")
        dataframes[table_name] = load_csv(file_name, raw_data_dir)

    return dataframes