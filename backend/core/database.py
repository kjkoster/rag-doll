from os import environ
from sqlmodel import SQLModel, create_engine


def get_db_url():
    TESTING = environ.get("TESTING")
    DATABASE_URL = environ["DATABASE_URL"]
    DB_URL = f"{DATABASE_URL}_test" if TESTING else DATABASE_URL
    return DB_URL


engine = create_engine(get_db_url(), echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
