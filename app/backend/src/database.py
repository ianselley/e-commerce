from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://{user}:{pwd}@{host}:{port}/{db}".format(
    user=os.getenv("MYSQL_USER"),
    pwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=os.getenv("MYSQL_PORT"),
    db=os.getenv("MYSQL_DATABASE"),
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()