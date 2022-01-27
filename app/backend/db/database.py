from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core import config


SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://{user}:{pwd}@{host}:{port}/{db}".format(
    user=config.MYSQL_USER,
    pwd=config.MYSQL_PASSWORD,
    host=config.MYSQL_HOST,
    port=config.MYSQL_PORT,
    db=config.MYSQL_DATABASE,
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

Base = declarative_base()