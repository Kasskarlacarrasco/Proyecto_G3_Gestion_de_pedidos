// frontend/src/pages/ImportPedidosPage.tsx
import { useEffect, useState } from "react";
import type { ChangeEvent } from "react";
import { api } from "../api/client";

interface Pedido {
  id: number;
  estado?: string | null;

  codigo_pedido?: string | null;
  usuario?: string | null;
  correo?: string | null;
  celular?: string | null;

  sku?: string | null;
  producto?: string | null;
  categoria?: string | null;

  cantidad?: number | null;
  precio?: number | null;
  precio_total?: number | null;

  tipo_despacho?: string | null;
  direccion_entrega?: string | null;
  referencia?: string | null;
  distrito?: string | null;
  persona_contacto?: string | null;
  numero_contacto?: string | null;
  dedicatoria?: string | null;

  fecha_entrega?: string | null;
  hora_entrega?: string | null;

  tipo_recibo?: string | null;
  numero_documento?: number | null;
  razon_social?: string | null;
  direccion_facturacion?: string | null;

  metodo_pago?: string | null;
  codigo_transaccion?: string | number | null;

  subtotal?: number | null;
  recargo_envio?: number | null;
  total?: number | null;
}

const ImportPedidosPage = () => {
  const [file, setFile] = useState<File | null>(null);
  const [mensaje, setMensaje] = useState<string>("");
  const [cargandoUpload, setCargandoUpload] = useState<boolean>(false);
  const [cargandoLista, setCargandoLista] = useState<boolean>(false);
  const [pedidos, setPedidos] = useState<Pedido[]>([]);

  // Cargar lista de pedidos al montar el componente
  const cargarPedidos = async () => {
    try {
      setCargandoLista(true);
      const res = await api.get<Pedido[]>("/pedidos");
      setPedidos(res.data);
    } catch (error) {
      console.error(error);
      setMensaje("Error al cargar la lista de pedidos");
    } finally {
      setCargandoLista(false);
    }
  };

  useEffect(() => {
    cargarPedidos();
  }, []);

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
      setMensaje("");
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setMensaje("Selecciona un archivo Excel primero");
      return;
    }

    try {
      setCargandoUpload(true);
      setMensaje("");

      const formData = new FormData();
      formData.append("file", file);

      const res = await api.post("/pedidos/importar-excel", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      setMensaje(`Importados: ${res.data.resumen.importados}`);
      await cargarPedidos();
    } catch (error) {
      console.error(error);
      setMensaje("Error al importar el Excel de pedidos");
    } finally {
      setCargandoUpload(false);
    }
  };

  const formatMoney = (value?: number | null) => {
    if (typeof value === "number") {
      return `S/ ${value.toFixed(2)}`;
    }
    return "-";
  };

  return (
    <div
      style={{
        padding: "24px",
        fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI'",
        backgroundColor: "#121212",
        minHeight: "100vh",
        color: "#f5f5f5",
      }}
    >
      <h1 style={{ marginBottom: "16px" }}>Gestión de Pedidos</h1>

      {/* Panel de carga */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: "12px",
          marginBottom: "20px",
          backgroundColor: "#1e1e1e",
          padding: "16px",
          borderRadius: "8px",
          border: "1px solid #333",
        }}
      >
        <div>
          <input
            type="file"
            accept=".xlsx,.xls"
            onChange={handleFileChange}
            style={{ color: "#f5f5f5" }}
          />
        </div>
        <button
          onClick={handleUpload}
          disabled={cargandoUpload}
          style={{
            backgroundColor: cargandoUpload ? "#555" : "#1976d2",
            border: "none",
            color: "#fff",
            padding: "8px 16px",
            borderRadius: "4px",
            cursor: cargandoUpload ? "default" : "pointer",
            fontWeight: 500,
          }}
        >
          {cargandoUpload ? "Subiendo..." : "Subir Excel"}
        </button>
        {mensaje && (
          <span
            style={{
              marginLeft: "12px",
              fontSize: "0.9rem",
              color: mensaje.startsWith("Error") ? "#ff6666" : "#8bc34a",
            }}
          >
            {mensaje}
          </span>
        )}
      </div>

      {/* Tabla de pedidos */}
      <div
        style={{
          backgroundColor: "#1a1a1a",
          borderRadius: "8px",
          border: "1px solid #333",
          padding: "12px",
        }}
      >
        <div
          style={{
            marginBottom: "8px",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            fontSize: "0.9rem",
            color: "#bbb",
          }}
        >
          <span>Lista de pedidos (últimos {pedidos.length})</span>
          {cargandoLista && <span>Cargando lista...</span>}
        </div>

        <div
          style={{
            overflowX: "auto",
            maxHeight: "60vh",
            overflowY: "auto",
          }}
        >
          <table
            style={{
              width: "100%",
              borderCollapse: "collapse",
              fontSize: "0.78rem",
            }}
          >
            <thead>
              <tr
                style={{
                  backgroundColor: "#262626",
                  color: "#f5f5f5",
                  textAlign: "left",
                }}
              >
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Código de Pedido
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Usuario
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Correo
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Celular
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  SKU
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Producto
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Categoría
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Cantidad
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Precio
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Precio Total
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Tipo de despacho
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Dirección de entrega
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Referencia
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Distrito
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Persona de contacto
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Número de contacto
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Dedicatoria
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Fecha de entrega
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Hora de entrega
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Tipo de recibo
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Número de documento
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Razón Social
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Dirección de facturación
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Método de Pago
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Código de transacción
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Subtotal
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Recargo por envío
                </th>
                <th style={{ padding: "8px", borderBottom: "1px solid #333" }}>
                  Total
                </th>
              </tr>
            </thead>
            <tbody>
              {pedidos.length === 0 && !cargandoLista && (
                <tr>
                  <td
                    colSpan={28}
                    style={{
                      padding: "12px",
                      textAlign: "center",
                      color: "#888",
                    }}
                  >
                    No hay pedidos registrados.
                  </td>
                </tr>
              )}

              {pedidos.map((p) => {
                let bg = "#181818";
                if (p.estado === "CONFIRMADO") bg = "#1b3c2b";
                else if (p.estado === "SIN_STOCK") bg = "#3c1b1b";
                else if (p.estado?.startsWith("SIN_")) bg = "#3c2b1b";

                return (
                  <tr key={p.id} style={{ backgroundColor: bg }}>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.codigo_pedido || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.usuario || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.correo || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.celular || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.sku || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.producto || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.categoria || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.cantidad ?? "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {formatMoney(p.precio)}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {formatMoney(p.precio_total)}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.tipo_despacho || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.direccion_entrega || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.referencia || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.distrito || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.persona_contacto || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.numero_contacto || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.dedicatoria || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.fecha_entrega || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.hora_entrega || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.tipo_recibo || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.numero_documento ?? "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.razon_social || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.direccion_facturacion || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.metodo_pago || "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {p.codigo_transaccion ?? "-"}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {formatMoney(p.subtotal)}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {formatMoney(p.recargo_envio)}
                    </td>
                    <td style={{ padding: "6px 8px", borderBottom: "1px solid #262626" }}>
                      {formatMoney(p.total)}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default ImportPedidosPage;
