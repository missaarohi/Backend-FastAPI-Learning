import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = os.getenv("DATABASE_URL", "sqlite:///./test.db")

if db_url.startswith("sqlite"):
    engine = create_engine(db_url, connect_args={"check_same_thread": False})
else:
    engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)