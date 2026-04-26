import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

#endpoint object with season parameter



#-----extract data from api-----
def extract_data():
    
    endpoint=leaguedashteamstats.LeagueDashTeamStats(season="2024-25")#endpoint obect with season parameter
    df = endpoint.get_data_frames()[0]
    
   
    
    return df
    
