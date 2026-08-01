# Basketball Data Pipeline

An end-to-end data pipeline that pulls live NBA team stats from the NBA API, 
cleans and transforms the data, stores it in a SQLite database, 
and visualizes it through a Streamlit dashboard.

## Project Structure
Minimal ETL pipeline for scraping basic NBA team stats, transforming them, and loading into a SQLite database.

## Requirements

Install the runtime dependencies (prefer a virtual environment):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Notes: `requirements.txt` lists the minimal packages used by this project: `pandas`, `SQLAlchemy`, `schedule`, `nba_api`, `streamlit`, and `pytest`.

## Run the pipeline

Run the pipeline script directly. The scheduler loop in `main.py` is guarded so imports won't run the scheduler when the package is imported.

```powershell
python main.py
```

`main.py` calls `run_pipeline()` once at startup and (when run as a script) keeps a scheduler loop to run periodically.

## Tests

Run the pytest suite (uses an in-memory SQLite DB for isolation):

```powershell
pytest -q
```

## Files

- `main.py` — orchestrator and scheduler guard.
- `pipeline/extract.py` — calls `nba_api` and returns a DataFrame; includes basic validation.
- `pipeline/transform.py` — simple cleaning and selection of columns.
- `pipeline/load.py` — transactional writes using SQLAlchemy `engine.begin()`.
- `tests/` — smoke and pytest test to validate basic pipeline flow.

## Notes & Troubleshooting

- If the editor reports "Import 'schedule' could not be resolved", install packages from `requirements.txt` and reload the editor's Python interpreter.
- The database used by default is `basketball.db` (SQLite). For tests we use `sqlite:///:memory:` to avoid side effects.

If you'd like the README expanded with examples, diagrams, or pinned dependency versions, tell me which part to expand.
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
