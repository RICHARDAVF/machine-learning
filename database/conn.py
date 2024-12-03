from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
URL_DATABASE = "sqlite:///./data_sbs.db"
engine = create_engine(URL_DATABASE,connect_args={"check_same_thread":False})
SESSION_LOCAL = sessionmaker(autocommit=False,autoflush=False,bind=engine)

db = SESSION_LOCAL()