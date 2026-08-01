
# Basketball Data Pipeline

An end-to-end data pipeline that pulls live NBA team stats from the NBA API,
cleans and transforms the data, stores it in a SQLite database,
and visualizes it through a Streamlit dashboard.

## Why I Built This

I wanted to understand what actually separates winning teams from losing
ones beyond just looking at the scoreboard. This pipeline pulls real NBA
team stats and breaks them down into shooting efficiency, defensive
performance, and win percentage so you can see which teams win through
defense, which win through scoring, and which are overperforming or
underperforming relative to their stats. It started as a way to practice
data engineering fundamentals, but it ended up being a genuinely useful
way to explore what drives winning in the NBA.

## Project Structure

```
basketball d_pipeline/
├── main.py           # orchestrator and scheduler guard
├── dashboard.py       # Streamlit dashboard
├── querries.py         # analytical SQL queries
├── requirements.txt   # project dependencies
├── pipeline/
│   ├── extract.py     # pulls data from the NBA API
│   ├── transform.py   # cleans and splits data into shooting/defensive/performance
│   └── load.py        # writes to SQLite in a single transaction
└── tests/
    ├── smoke_test.py   # manual end-to-end sanity check
    └── test_pipeline.py # pytest suite
```

## Requirements

Install the runtime dependencies (prefer a virtual environment):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

`requirements.txt` lists the packages used by this project: `pandas`, `SQLAlchemy`, `schedule`, `nba_api`, `streamlit`, and `pytest`.

## Usage

**1. Run the pipeline** — pulls live data and (re)creates `basketball.db` locally:

```powershell
python main.py
```

`main.py` calls `run_pipeline()` once at startup and, when run as a script, keeps a scheduler loop running to refresh the data daily. `basketball.db` isn't committed to the repo (it's a generated artifact, listed in `.gitignore`) — this step creates it from scratch on your machine.

**2. View the dashboard** — reads from `basketball.db`, so run the pipeline at least once first:

```powershell
streamlit run dashboard.py
```

This opens automatically in your default browser at `http://localhost:8501` (also printed in the terminal).

## Tests

Run the pytest suite (uses an in-memory SQLite DB for isolation, so it never touches your real `basketball.db`):

```powershell
pytest -q
```

## Dashboard

- **Defensive Stats** — teams ranked by combined steals and blocks
- **Above Average Win Percentage** — teams with win percentage above the league average
- **Shooting Proficiency** — teams ranked by field goal percentage

## Notes & Troubleshooting

- If the editor reports "Import 'schedule' could not be resolved", install packages from `requirements.txt` and reload the editor's Python interpreter.
- The database used by default is `basketball.db` (SQLite). Tests use `sqlite:///:memory:` to avoid side effects.

## What I Learned

- How to build an end-to-end data pipeline from scratch
- How to pull live data from a public API
- How to clean, transform, and split data into multiple tables
- How to store data using SQLite and SQLAlchemy
- Why SQLAlchemy matters — it makes switching between databases easy
- Basic to intermediate SQL — SELECT, JOIN, subqueries, aggregations
- How to schedule automated pipeline runs
- How to build an interactive dashboard with Streamlit
