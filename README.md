# Basketball Data Pipeline

An end-to-end data pipeline that pulls live NBA team stats from the NBA API, 
cleans and transforms the data, stores it in a SQLite database, 
and visualizes it through a Streamlit dashboard.

## Project Structure
project1/
├── main.py          # runs the full pipeline
├── dashboard.py     # Streamlit dashboard
├── queries.py       # analytical SQL queries
├── requirements.txt # project dependencies
└── pipeline/
    ├── extract.py   # pulls data from NBA API
    ├── transform.py # cleans and splits data
    └── load.py      # saves to SQLite database

## Installation

Install all dependencies with:
pip install -r requirements.txt

## How to Run

### Run the pipeline
python main.py

### View the dashboard
streamlit run dashboard.py

## Dashboard

- **Defensive Stats** — teams ranked by combined steals and blocks
- **Win Percentage** — teams with above average win percentage
- **Shooting Efficiency** — teams ranked by field goal percentage

## What I Learned

- How to build an end-to-end data pipeline from scratch
- How to pull live data from a public API
- How to clean, transform, and split data into multiple tables
- How to store data using SQLite and SQLAlchemy
- Why SQLAlchemy matters — it makes switching between databases easy
- Basic to intermediate SQL — SELECT, JOIN, subqueries, aggregations
- How to schedule automated pipeline runs
- How to build an interactive dashboard with Streamlit