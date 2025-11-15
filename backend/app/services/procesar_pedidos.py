# backend/app/services/procesar_pedidos.py
from sqlalchemy.orm import Session
from sqlalchemy import asc
from decimal import Decimal

from ..models.pedidos import Pedido
from ..models.stock import Stock
from ..models.distritos import DistritoTienda


def procesar_pedidos_con_stock(db: Session):
    """
    Recorre pedidos ordenados por fecha, asigna tienda por distrito
    y descuenta stock en la tabla stock. Actualiza el campo 'estado'
    del pedido a CONFIRMADO o SIN_STOCK.
    """

    # Traer todos los pedidos en orden cronológico
    pedidos = (
        db.query(Pedido)
        .order_by(asc(Pedido.fecha_registro))
        .all()
    )

    procesados = 0
    confirmados = 0
    sin_stock = 0
    sin_mapeo_distrito = 0
    sin_producto = 0

    for pedido in pedidos:
        procesados += 1

        # 1) Buscar tienda según distrito
        distrito_nombre = (pedido.distrito or "").strip()

        if not distrito_nombre:
            pedido.estado = "SIN_DISTRITO"
            sin_mapeo_distrito += 1
            continue

        distrito_tienda = (
            db.query(DistritoTienda)
            .filter(DistritoTienda.distrito == distrito_nombre)
            .first()
        )

        if not distrito_tienda:
            # No se encontró tienda para ese distrito
            pedido.estado = "SIN_TIENDA_PARA_DISTRITO"
            sin_mapeo_distrito += 1
            continue

        tienda_nombre = (distrito_tienda.tienda or "").strip()

        # 2) Buscar stock del SKU en esa tienda
        sku = (pedido.sku or "").strip()
        if not sku:
            pedido.estado = "SIN_SKU"
            sin_producto += 1
            continue

        stock_item = (
            db.query(Stock)
            .filter(
                Stock.FS_DES_SUCU == tienda_nombre,
                Stock.FS_COD_ARTI == sku,
            )
            .first()
        )

        if not stock_item:
            # No hay stock cargado para ese SKU en esa tienda
            pedido.estado = "SIN_STOCK"
            sin_producto += 1
            continue

        cantidad_pedido = pedido.cantidad or 0
        stock_actual = stock_item.FN_CAN_ACTU or Decimal("0")

        # Asegurar tipo Decimal para operar
        if isinstance(stock_actual, float):
            stock_actual = Decimal(str(stock_actual))

        # 3) Verificar stock suficiente
        if stock_actual >= Decimal(cantidad_pedido):
            # Descontar stock
            stock_item.FN_CAN_ACTU = stock_actual - Decimal(cantidad_pedido)
            pedido.estado = "CONFIRMADO"
            confirmados += 1
        else:
            pedido.estado = "SIN_STOCK"
            sin_stock += 1

    db.commit()

    return {
        "procesados": procesados,
        "confirmados": confirmados,
        "sin_stock": sin_stock,
        "sin_mapeo_distrito": sin_mapeo_distrito,
        "sin_producto": sin_producto,
    }
