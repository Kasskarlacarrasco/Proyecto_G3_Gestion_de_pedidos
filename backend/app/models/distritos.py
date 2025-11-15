# backend/app/models/distritos.py
from sqlalchemy import Column, Integer, String
from ..core.database import Base

class DistritoTienda(Base):
    __tablename__ = "distritosxtienda"

    id = Column(Integer, primary_key=True, index=True)
    tienda = Column(String(150))
    distrito = Column(String(150))
