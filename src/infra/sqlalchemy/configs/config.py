from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine



# recomendavel utilizar MySQL pois é bem mais rapido
SQLALCHEMY_DATABASE_URL = "nome do banco MySQL ou sqlite"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def criar_db():
    Base.metadata.create_all(bind=engine)