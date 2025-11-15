# backend/app/api/stock.py
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..services.import_stock import procesar_excel_stock

router = APIRouter(prefix="/stock", tags=["Stock"])

@router.post("/importar-excel")
async def importar_stock(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contenido = await file.read()
    resumen = procesar_excel_stock(contenido, db)
    return {"status": "ok", "resumen": resumen}
