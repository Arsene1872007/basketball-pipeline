import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

# endpoint object with season parameter


# -----extract data from api-----
def extract_data(season: str = "2024-25") -> pd.DataFrame:
    try:
        endpoint = leaguedashteamstats.LeagueDashTeamStats(season=season)
        frames = endpoint.get_data_frames()
    except Exception as exc:
        raise RuntimeError(f"NBA API extraction failed for season {season}: {exc}") from exc

    if not frames:
        raise ValueError(f"NBA API returned no data frames for season {season}")

    df = frames[0]
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Expected the NBA API endpoint to return a pandas DataFrame")

    return df
    
