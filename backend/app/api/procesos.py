# backend/app/api/procesos.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..services.procesar_pedidos import procesar_pedidos_con_stock

router = APIRouter(prefix="/procesos", tags=["Procesos"])

@router.post("/procesar-pedidos")
def procesar_pedidos(db: Session = Depends(get_db)):
    resumen = procesar_pedidos_con_stock(db)
    return {
        "status": "ok",
        "mensaje": "Proceso de cruce pedidos vs stock completado",
        "resumen": resumen,
    }
