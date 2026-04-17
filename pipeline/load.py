from sqlalchemy import create_engine
import pandas as pd

def load_data(df):
    
    engine = create_engine("sqlite:///basketball.db")
    df.to_sql("players",engine,if_exists="replace")

    return df