from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

db_host = "db"
db_name = os.environ.get("MYSQL_DATABASE")
db_user = os.environ.get("MYSQL_USER")
db_password = os.environ.get("MYSQL_PASSWORD")

engine = create_engine(f"mariadb+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}", echo=True)

DBSession = sessionmaker(engine, autoflush=False)
