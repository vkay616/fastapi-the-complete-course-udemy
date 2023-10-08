from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://root:{environ["MYSQL_PASSWORD"]}@127.0.0.1:3306/todoapplicationdatabase'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

