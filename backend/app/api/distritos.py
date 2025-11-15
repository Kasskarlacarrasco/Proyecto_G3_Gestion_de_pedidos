# backend/app/api/distritos.py
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..services.import_distritos import procesar_excel_distritos

router = APIRouter(prefix="/distritos", tags=["Distritos"])

@router.post("/importar-excel")
async def importar_distritos(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contenido = await file.read()
    resumen = procesar_excel_distritos(contenido, db)
    return {"status": "ok", "resumen": resumen}
