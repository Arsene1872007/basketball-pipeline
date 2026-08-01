from pipeline.extract import extract_data
from pipeline.transform import  delete_empty, get_shooting_stats,get_defensive_stats,get_performance
from pipeline.load import load_data
import schedule
import time

def run_pipeline():
  print("running pipeline")
  df = extract_data()
  df = delete_empty(df)
  shooting = get_shooting_stats(df)
  defensive = get_defensive_stats(df)
  performance = get_performance(df)
  load_data(shooting,defensive,performance)
  print("pipeline completed")


if __name__ == "__main__":
  print("scheduling job")
  schedule.every().day.at("08:00").do(run_pipeline)
  run_pipeline()
  while True:
      schedule.run_pending()  #checks if any scheduled jobs are due at the moment
      time.sleep(60)

