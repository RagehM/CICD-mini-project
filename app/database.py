from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from pathlib import Path

# Create the database directory if it doesn't exist
DB_DIR = Path("./data")
DB_DIR.mkdir(exist_ok=True)

DATABASE_URL = f"sqlite:///{DB_DIR}/students.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False  # Set to True for SQL query logging
)

# Create sessionmaker with modern configuration
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False  # Modern SQLAlchemy best practice
)

# Create declarative base
Base = declarative_base()
