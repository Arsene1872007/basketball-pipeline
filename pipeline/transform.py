#-----removes empty rows-----
def delete_empty(df):
    #checks and sums all the number of missing values
    missing_values = df.isnull().sum().sum()

    #deletes the missing values
    clean_data=df.dropna(subset=["PTS","FGA","STL","REB","W","L"])
    print("There is a total of ", missing_values, " missing values in this dataset")
    return clean_data


def get_shooting_stats(df):
    shooting=df[['TEAM_NAME','FGM', 'FGA','FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT','PTS']]
    return shooting

def get_defensive_stats(df):
    defense=df[['TEAM_NAME','OREB','DREB', 'REB', 'AST', 'TOV','STL', 'BLK', 'BLKA','PF']]
    
    return defense
def get_performance(df):
    performmance=df[['TEAM_NAME','W', 'L','W_PCT','PLUS_MINUS','GP_RANK', 'W_RANK', 'L_RANK', 'W_PCT_RANK', 'MIN_RANK',
       'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK',
       'FG3_PCT_RANK', 'FTM_RANK', 'FTA_RANK', 'FT_PCT_RANK', 'OREB_RANK',
       'DREB_RANK', 'REB_RANK', 'AST_RANK', 'TOV_RANK', 'STL_RANK', 'BLK_RANK',
       'BLKA_RANK', 'PF_RANK', 'PFD_RANK', 'PTS_RANK', 'PLUS_MINUS_RANK']]
    return performmance
