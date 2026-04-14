from pipeline.extract import extract_data
from pipeline.transform import create_column, delete_empty, filter_data


def run_pipeline():
    df = extract_data()
    df = delete_empty(df)
    df = filter_data(df)
    df = create_column(df)
    return df


if __name__ == "__main__":
    df = run_pipeline()
    print(df.head())

