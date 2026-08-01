from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd


def load_data(shooting: pd.DataFrame, defense: pd.DataFrame, performance: pd.DataFrame, db_url: str = "sqlite:///basketball.db") -> bool:
    """Write the three dataframes to the database in a single transaction.

    Raises a TypeError if inputs are not DataFrames and RuntimeError on DB failures.
    Returns True on success.
    """
    # validate inputs
    for name, df in (("shooting", shooting), ("defense", defense), ("performance", performance)):
        if not isinstance(df, pd.DataFrame):
            raise TypeError(f"{name} must be a pandas DataFrame")

    engine = create_engine(db_url)
    try:
        # use a transaction so the three writes are atomic
        with engine.begin() as conn:
            shooting.to_sql("shooting", conn, if_exists="replace", index=False)
            defense.to_sql("defensive", conn, if_exists="replace", index=False)
            performance.to_sql("performance", conn, if_exists="replace", index=False)
    except SQLAlchemyError as exc:
        raise RuntimeError(f"Database write failed: {exc}") from exc
    finally:
        engine.dispose()

    return True