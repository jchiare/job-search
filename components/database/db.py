from dotenv import find_dotenv, load_dotenv
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def load_environment_variables():
    """
    Load environment variables from the .env file.
    """
    load_dotenv(find_dotenv())


def create_db_engine():
    load_environment_variables()

    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USERNAME")
    passwd = os.getenv("DB_PASSWORD")
    db = (
        os.getenv("DB_NAME")
        if os.getenv("PROD_DB") == "true"
        else os.getenv("DEV_DB_NAME")
    )
    connection_string = f"mysql+mysqlconnector://{user}:{passwd}@{host}:3306/{db}"
    engine = create_engine(connection_string, echo=True)
    return engine


db = create_db_engine()
SessionLocal = sessionmaker(bind=db)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
