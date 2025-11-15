# backend/app/services/import_stock.py
from io import BytesIO
import math
import pandas as pd
from sqlalchemy.orm import Session
from ..models.stock import Stock


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

    # Cualquier NA detectado por pandas
    if pd.isna(value):
        return None

    return value


def procesar_excel_stock(file_bytes: bytes, db: Session):
    # Leer Excel
    df = pd.read_excel(BytesIO(file_bytes), engine="openpyxl")
    print("Columnas Excel Stock:", df.columns.tolist())

    contador = 0

    for _, row in df.iterrows():
        stock_item = Stock(
            FS_COD_SUCU=_clean_value(row.get("FS_COD_SUCU")),
            FS_DES_SUCU=_clean_value(row.get("FS_DES_SUCU")),
            FS_COD_ALMA=_clean_value(row.get("FS_COD_ALMA")),
            FS_DES_ALMA=_clean_value(row.get("FS_DES_ALMA")),
            FS_COD_UBIC_ALMA=_clean_value(row.get("FS_COD_UBIC_ALMA")),
            FS_COD_CLAS_0001=_clean_value(row.get("FS_COD_CLAS_0001")),
            FS_DES_CLAS_0001=_clean_value(row.get("FS_DES_CLAS_0001")),
            FS_COD_CLAS_0002=_clean_value(row.get("FS_COD_CLAS_0002")),
            FS_DES_CLAS_0002=_clean_value(row.get("FS_DES_CLAS_0002")),
            FS_COD_CLAS_0003=_clean_value(row.get("FS_COD_CLAS_0003")),
            FS_DES_CLAS_0003=_clean_value(row.get("FS_DES_CLAS_0003")),
            FS_COD_CLAS_0004=_clean_value(row.get("FS_COD_CLAS_0004")),
            FS_DES_CLAS_0004=_clean_value(row.get("FS_DES_CLAS_0004")),
            FS_COD_MARC=_clean_value(row.get("FS_COD_MARC")),
            FS_DES_MARC=_clean_value(row.get("FS_DES_MARC")),
            FS_COD_ARTI=_clean_value(row.get("FS_COD_ARTI")),
            FN_CAN_ACTU=_clean_value(row.get("FN_CAN_ACTU")),
            FS_DES_ARTI=_clean_value(row.get("FS_DES_ARTI")),
            FS_DES_ARTI_LARG=_clean_value(row.get("FS_DES_ARTI_LARG")),
            FS_COD_UNME=_clean_value(row.get("FS_COD_UNME")),
            AGRUPACION=_clean_value(row.get("AGRUPACION")),
            FS_CLA_CLAS_PLAN=_clean_value(row.get("FS_CLA_CLAS_PLAN")),
            FN_NUM_PESO=_clean_value(row.get("FN_NUM_PESO")),
            FN_NUM_VOLU=_clean_value(row.get("FN_NUM_VOLU")),
            FS_COD_UNME_ALTE=_clean_value(row.get("FS_COD_UNME_ALTE")),
            FN_CAN_ACTU_ALTE=_clean_value(row.get("FN_CAN_ACTU_ALTE")),
            FS_COD_UNME_EMPA=_clean_value(row.get("FS_COD_UNME_EMPA")),
            FN_CAN_EMPA=_clean_value(row.get("FN_CAN_EMPA")),
            FN_CAN_EMPA_UNID=_clean_value(row.get("FN_CAN_EMPA_UNID")),
            FS_SEL_UNID_MEDI=_clean_value(row.get("FS_SEL_UNID_MEDI")),
            FN_CAN_LOTE=_clean_value(row.get("FN_CAN_LOTE")),
            FS_STA_CANT_LOTE=_clean_value(row.get("FS_STA_CANT_LOTE")),
            FS_COD_ARTI_ALTE=_clean_value(row.get("FS_COD_ARTI_ALTE")),
            FS_DES_TAMA=_clean_value(row.get("FS_DES_TAMA")),
            FS_COD_GENE=_clean_value(row.get("FS_COD_GENE")),
            FS_COD_ATNI_AT01=_clean_value(row.get("FS_COD_ATNI_AT01")),
            FS_DES_ATNI_AT01=_clean_value(row.get("FS_DES_ATNI_AT01")),
            FS_COD_ATNI_NI01=_clean_value(row.get("FS_COD_ATNI_NI01")),
            FS_DES_ATNI_NI01=_clean_value(row.get("FS_DES_ATNI_NI01")),
            FS_COD_ATRI_0001=_clean_value(row.get("FS_COD_ATRI_0001")),
            FS_DES_ATRI_0001=_clean_value(row.get("FS_DES_ATRI_0001")),
            FS_COD_ATRI_0002=_clean_value(row.get("FS_COD_ATRI_0002")),
            FS_DES_ATRI_0002=_clean_value(row.get("FS_DES_ATRI_0002")),
            FS_COD_ATRI_0003=_clean_value(row.get("FS_COD_ATRI_0003")),
            FS_DES_ATRI_0003=_clean_value(row.get("FS_DES_ATRI_0003")),
            FS_COD_ATRI_0004=_clean_value(row.get("FS_COD_ATRI_0004")),
            FS_DES_ATRI_0004=_clean_value(row.get("FS_DES_ATRI_0004")),
            FS_DES_GENE=_clean_value(row.get("FS_DES_GENE")),
            FS_DES_RUTA_IMAG=_clean_value(row.get("FS_DES_RUTA_IMAG")),
            FS_DES_LABO=_clean_value(row.get("FS_DES_LABO")),
            FI_COD_EMPR=_clean_value(row.get("FI_COD_EMPR")),
            FS_DES_EMPR=_clean_value(row.get("FS_DES_EMPR")),
        )

        db.add(stock_item)
        contador += 1

    db.commit()
    return {"importados": contador}
