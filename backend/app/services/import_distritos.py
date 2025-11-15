# backend/app/services/import_distritos.py
from io import BytesIO
import math
import pandas as pd
from sqlalchemy.orm import Session
from ..models.distritos import DistritoTienda


def _clean_value(value):
    """Limpia valores NaN/NaT para que MySQL los acepte como NULL."""
    if value is None:
        return None

    # Floats NaN
    try:
        if isinstance(value, float) and math.isnan(value):
            return None
    except TypeError:
        pass

    # Cualquier NA reconocido por pandas
    if pd.isna(value):
        return None

    return value


def procesar_excel_distritos(file_bytes: bytes, db: Session):
    # Leer Excel desde bytes
    df = pd.read_excel(BytesIO(file_bytes), engine="openpyxl")
    print("Columnas Excel Distritos:", df.columns.tolist())

    contador = 0
    for _, row in df.iterrows():
        registro = DistritoTienda(
            tienda=_clean_value(row.get("TIENDA")),
            distrito=_clean_value(row.get("DISTRITO")),
        )
        db.add(registro)
        contador += 1

    db.commit()
    return {"importados": contador}
