import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
try:
    engine=create_engine("sqlite:///basketball.db")

    st.title("MY DASHBOARD")

    st.header("DEFENSIVE STATS")

    #-----TEAMS defensive stats ranked from best
    query1="""
        SELECT TEAM_NAME,STL+BLK as combined_defense
        FROM defensive
        ORDER BY combined_defense DESC
    
    """

    df1=pd.read_sql(query1,engine)
    st.dataframe(df1)
    st.bar_chart(df1.set_index("TEAM_NAME"))


    st.text(" stats showing teams defensive capabilities ranked from best based on the total steals and blocks ")

    st.header("ABOVE AVERAGE WIN PERCENTAGE")

    query2="""
        SELECT p.TEAM_NAME,s.PTS,p.W_PCT
        FROM shooting s
        JOIN performance p ON p.TEAM_NAME=s.TEAM_NAME
        WHERE W_PCT>(SELECT AVG(W_PCT) FROM performance)
        ORDER BY W_PCT DESC
        
    """

    df2=pd.read_sql(query2,engine)
    st.dataframe(df2)
    st.text("shows teams with a above average win probability based on point and their win percentage")


    st.header("SHOOTING PROFICIENCY")
    query3="""
        SELECT TEAM_NAME, FG_PCT, FG3_PCT, FT_PCT 
        FROM shooting
        ORDER BY FG_PCT DESC
    """

    df3=pd.read_sql(query3,engine)
    st.dataframe(df3)
    st.bar_chart(df3.set_index("TEAM_NAME"))

    st.text("shows shooting proficiency based on their field goal percentage ")

except Exception as e:
    st.error(f"Dashboard failed to load: {e}")