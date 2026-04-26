from pipeline.extract import extract_data
from pipeline.transform import  delete_empty, get_shooting_stats,get_defensive_stats,get_performance
from pipeline.load import load_data

def run_pipeline():
    df = extract_data()
    df = delete_empty(df)
    shooting = get_shooting_stats(df)
    defensive = get_defensive_stats(df)
    performance = get_performance(df)
    load_data(shooting,defensive,performance)
    print("pipeline completed")


if __name__ == "__main__":
    try:
        run_pipeline()
    except Exception as e:
        print("pipeline failed with",e)
       
