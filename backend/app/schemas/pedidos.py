# backend/app/schemas/pedidos.py
from datetime import datetime, date
from pydantic import BaseModel


class PedidoRead(BaseModel):
    id: int

    codigo_pedido: str | None = None
    estado: str | None = None

    usuario: str | None = None
    correo: str | None = None
    celular: str | None = None

    sku: str | None = None
    producto: str | None = None
    categoria: str | None = None

    cantidad: int | None = None
    precio: float | None = None
    precio_total: float | None = None

    tipo_despacho: str | None = None
    direccion_entrega: str | None = None
    referencia: str | None = None
    distrito: str | None = None
    persona_contacto: str | None = None
    numero_contacto: str | None = None
    dedicatoria: str | None = None

    fecha_registro: datetime | None = None
    fecha_entrega: date | None = None
    hora_entrega: str | None = None

    tipo_recibo: str | None = None
    numero_documento: int | None = None
    razon_social: str | None = None
    direccion_facturacion: str | None = None

    metodo_pago: str | None = None
    codigo_transaccion: str | None = None  # aunque en BD sea numérico, aquí lo tratamos como string

    subtotal: float | None = None
    recargo_envio: float | None = None
    total: float | None = None

    class Config:
        from_attributes = True  # reemplaza orm_mode=True en Pydantic v2
