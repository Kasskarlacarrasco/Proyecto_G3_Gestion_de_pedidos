# backend/app/services/import_pedidos.py
from io import BytesIO
import math
import pandas as pd
from sqlalchemy.orm import Session
from ..models.pedidos import Pedido


def _clean_value(value):
    """Convierte cualquier NaN/NaT a None para que MySQL lo acepte como NULL."""
    if value is None:
        return None

    # Floats típicos de pandas/numpy (NaN)
    try:
        if isinstance(value, float) and math.isnan(value):
            return None
    except TypeError:
        pass

    # Cualquier otro tipo que pandas marque como NA
    if pd.isna(value):
        return None

    return value


def procesar_excel_pedidos(file_bytes: bytes, db: Session):
    # Leer el Excel desde memoria
    df = pd.read_excel(BytesIO(file_bytes), engine="openpyxl")

    print("Columnas del Excel:", df.columns.tolist())

    contador = 0
    for _, row in df.iterrows():
        pedido = Pedido(
            codigo_pedido=_clean_value(row.get("Código de Pedido")),
            estado=_clean_value(row.get("Estado")),
            fecha_registro=_clean_value(row.get("Fecha de Registro")),
            cupon=_clean_value(row.get("Cupón")),
            nombre_promocion=_clean_value(row.get("Nombre promoción")),
            codigo_erp=_clean_value(row.get("Código ERP")),
            dispositivo=_clean_value(row.get("Dispositivo")),
            navegador=_clean_value(row.get("Navegador")),
            sistema_operativo=_clean_value(row.get("Sistema Operativo")),
            ip=_clean_value(row.get("IP")),
            modelo_dispositivo=_clean_value(row.get("Modelo de Dispositivo")),
            usuario=_clean_value(row.get("Usuario")),
            correo=_clean_value(row.get("Correo")),
            celular=_clean_value(row.get("Celular")),
            lista_precio=_clean_value(row.get("Lista de precio")),
            vendedor=_clean_value(row.get("Vendedor")),
            sku=_clean_value(row.get("SKU")),
            codigo_corto=_clean_value(row.get("Código Corto")),
            producto=_clean_value(row.get("Producto")),
            presentacion=_clean_value(row.get("Presentación")),
            subcategoria=_clean_value(row.get("Subcategoría")),
            categoria=_clean_value(row.get("Categoría")),
            cantidad=_clean_value(row.get("Cantidad")),
            precio=_clean_value(row.get("Precio")),
            precio_total=_clean_value(row.get("Precio Total")),
            almacen=_clean_value(row.get("Almacén")),
            tipo_despacho=_clean_value(row.get("Tipo de despacho")),
            direccion_entrega=_clean_value(row.get("Dirección de entrega")),
            referencia=_clean_value(row.get("Referencia")),
            distrito=_clean_value(row.get("Distrito")),
            persona_contacto=_clean_value(row.get("Persona de contacto")),
            numero_contacto=_clean_value(row.get("Número de contacto")),
            fecha_entrega=_clean_value(row.get("Fecha de entrega")),
            hora_entrega=_clean_value(row.get("Hora de entrega")),
            tipo_recibo=_clean_value(row.get("Tipo de recibo")),
            numero_documento=_clean_value(row.get("Número de documento")),
            razon_social=_clean_value(row.get("Razón Social")),
            direccion_facturacion=_clean_value(row.get("Dirección de facturación")),
            metodo_pago=_clean_value(row.get("Método de Pago")),
            codigo_transaccion=_clean_value(row.get("Código de transacción")),
            comentarios=_clean_value(row.get("Comentarios")),
            dedicatoria=_clean_value(row.get("Dedicatoria")),
            tarjeta_regalo=_clean_value(row.get("Tarjeta de regalo")),
            subtotal=_clean_value(row.get("Subtotal")),
            recargo_envio=_clean_value(row.get("Recargo por envío")),
            total=_clean_value(row.get("Total")),
            review_rating=_clean_value(row.get("Review Rating")),
        )

        db.add(pedido)
        contador += 1

    db.commit()
    return {"importados": contador}
