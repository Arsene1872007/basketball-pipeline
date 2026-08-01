import pandas as pd

from pipeline.transform import delete_empty, get_shooting_stats, get_defensive_stats, get_performance
from pipeline.load import load_data


def make_sample_df():
    data = {
        "TEAM_NAME": ["A", "B"],
        "FGM": [10, 9],
        "FGA": [20, 18],
        "FG_PCT": [0.5, 0.5],
        "FG3M": [2, 3],
        "FG3A": [5, 6],
        "FG3_PCT": [0.4, 0.5],
        "FTM": [5, 4],
        "FTA": [6, 5],
        "FT_PCT": [0.83, 0.8],
        "PTS": [40, 35],
        "OREB": [5, 4],
        "DREB": [20, 18],
        "REB": [25, 22],
        "AST": [10, 8],
        "TOV": [12, 11],
        "STL": [7, 6],
        "BLK": [3, 2],
        "BLKA": [1, 1],
        "PF": [18, 15],
        "W": [1, 0],
        "L": [0, 1],
        "W_PCT": [0.5, 0.0],
        "PLUS_MINUS": [3, -2],
        "GP_RANK": [1, 2],
        "W_RANK": [1, 2],
        "L_RANK": [2, 1],
        "W_PCT_RANK": [1, 2],
        "MIN_RANK": [10, 12],
        "FGM_RANK": [1, 2],
        "FGA_RANK": [1, 2],
        "FG_PCT_RANK": [1, 2],
        "FG3M_RANK": [1, 2],
        "FG3A_RANK": [1, 2],
        "FG3_PCT_RANK": [1, 2],
        "FTM_RANK": [1, 2],
        "FTA_RANK": [1, 2],
        "FT_PCT_RANK": [1, 2],
        "OREB_RANK": [1, 2],
        "DREB_RANK": [1, 2],
        "REB_RANK": [1, 2],
        "AST_RANK": [1, 2],
        "TOV_RANK": [1, 2],
        "STL_RANK": [1, 2],
        "BLK_RANK": [1, 2],
        "BLKA_RANK": [1, 2],
        "PF_RANK": [1, 2],
        "PFD_RANK": [1, 2],
        "PTS_RANK": [1, 2],
        "PLUS_MINUS_RANK": [1, 2],
    }
    return pd.DataFrame(data)


def run_smoke():
    df = make_sample_df()
    df_clean = delete_empty(df)
    shooting = get_shooting_stats(df_clean)
    defense = get_defensive_stats(df_clean)
    performance = get_performance(df_clean)

    # write to an in-memory DB to avoid filesystem side-effects
    load_data(shooting, defense, performance, db_url="sqlite:///:memory:")
    print("smoke test passed")


if __name__ == "__main__":
    run_smoke()
