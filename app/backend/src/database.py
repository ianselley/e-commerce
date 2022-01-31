from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import DATABASE


SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://{user}:{pwd}@{host}:{port}/{db}".format(
    user=DATABASE["MYSQL_USER"],
    pwd=DATABASE["MYSQL_PASSWORD"],
    host=DATABASE["MYSQL_HOST"],
    port=DATABASE["MYSQL_PORT"],
    db=DATABASE["MYSQL_DATABASE"],
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()