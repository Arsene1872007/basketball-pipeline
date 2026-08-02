import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///basketball.db")

# -----TEAMS defensive stats ranked from best
querry1 = """
    SELECT TEAM_NAME,STL+BLK as combined_defense
    FROM defensive
    ORDER BY combined_defense DESC
  
"""
print("Defense stats ranked from best")
df1 = pd.read_sql(querry1, engine)
print(df1)

querry2 = """
    SELECT p.TEAM_NAME,s.PTS,p.W_PCT
    FROM shooting s
    JOIN performance p ON p.TEAM_NAME=s.TEAM_NAME
    WHERE W_PCT>(SELECT AVG(W_PCT) FROM performance)
    ORDER BY W_PCT DESC
    
"""
print("Teams with above average win percentage")
df2 = pd.read_sql(querry2, engine)
print(df2)

querry3 = """
    SELECT TEAM_NAME, FG_PCT, FG3_PCT, FT_PCT 
    FROM shooting
    ORDER BY FG_PCT DESC
"""
print("shooting proficiency")
df3 = pd.read_sql(querry3, engine)
print(df3)
