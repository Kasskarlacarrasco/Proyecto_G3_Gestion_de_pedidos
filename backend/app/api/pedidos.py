# backend/app/api/pedidos.py
from typing import List
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from ..core.database import get_db
from ..services.import_pedidos import procesar_excel_pedidos
from ..models.pedidos import Pedido
from ..schemas.pedidos import PedidoRead

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.post("/importar-excel")
async def importar_pedidos(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contenido = await file.read()
    resumen = procesar_excel_pedidos(contenido, db)
    return {"status": "ok", "resumen": resumen}


@router.get("/", response_model=List[PedidoRead])
def listar_pedidos(db: Session = Depends(get_db)):
    """
    Lista los pedidos más recientes (por ejemplo últimos 200) para mostrar en el frontend.
    IMPORTANTE: MySQL/MariaDB no soporta 'NULLS LAST', así que solo usamos desc().
    """
    pedidos = (
        db.query(Pedido)
        .order_by(Pedido.fecha_registro.desc())  # <-- sin nullslast()
        .limit(200)
        .all()
    )
    return pedidos
