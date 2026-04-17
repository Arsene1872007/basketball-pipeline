from pipeline.extract import extract_data
from pipeline.transform import create_column, delete_empty, filter_data
from pipeline.load import load_data

def run_pipeline():
    df = extract_data()
    df = delete_empty(df)
    df = filter_data(df)
    df = create_column(df)
    df = load_data(df)
    return df


if __name__ == "__main__":
    try:
        df = run_pipeline()
        print(df.head())
    except Exception as e:
        print("pipeline failed:",e)
