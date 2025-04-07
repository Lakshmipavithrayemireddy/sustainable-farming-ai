from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager

DATABASE_URL = "sqlite:///farming.db"

# Create database engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()

@contextmanager
def get_db():
    """Context manager for database sessions."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initialize the database with tables."""
    Base.metadata.create_all(bind=engine)

def get_session():
    """Get a new database session."""
    return SessionLocal() 