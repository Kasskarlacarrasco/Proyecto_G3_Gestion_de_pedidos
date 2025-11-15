# backend/app/core/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

# Crear el engine de SQLAlchemy
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    future=True
)

# SessionLocal: para obtener sesiones de BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: clase base para los modelos
Base = declarative_base()

# Dependencia para FastAPI: obtener sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
