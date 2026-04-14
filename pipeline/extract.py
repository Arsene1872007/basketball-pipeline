import pandas as pd

#------loading csv-----
def extract_data():
    df = pd.read_csv("players_stats_by_season_full_details.csv")
    return df