from sqlalchemy import create_engine
import pandas as pd

def load_data(shooting, defense,performance):
    
    engine = create_engine("sqlite:///basketball.db")
    shooting.to_sql("shooting",engine,if_exists="replace")
    defense.to_sql("defensive",engine,if_exists="replace")
    performance.to_sql("performance",engine,if_exists="replace")
    
    return shooting,defense,performance