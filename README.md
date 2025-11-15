📦 Proyecto G3 – Gestión de Pedidos

Sistema completo para la carga masiva de pedidos desde Excel, validación de stock, actualización de estados y visualización desde una interfaz web.

Incluye:

✔ Backend en FastAPI + SQLAlchemy + MySQL/MariaDB

✔ Frontend en React + TypeScript

✔ Procesamiento de archivos Excel

✔ Gestión de pedidos, stock y distritos

✔ UI moderna con tema oscuro

🚀 Requisitos previos

Asegúrate de tener instalado:

✔ Python 3.10+
✔ Node.js 18+ y npm
✔ MySQL o MariaDB
✔ Git
📥 1. Clonar el proyecto
git clone https://github.com/Kasskarlacarrasco/Proyecto_G3_Gestion_de_pedidos.git
cd Proyecto_G3_Gestion_de_pedidos

🐍 2. Instalar y correr el Backend
📁 Navegar al directorio del backend:
cd backend

🧪 Crear entorno virtual:
python -m venv venv

🔧 Activar entorno virtual:

Windows PowerShell / Git Bash

source venv/Scripts/activate


CMD

venv\Scripts\activate


Linux / Mac

source venv/bin/activate

📦 Instalar dependencias:
pip install -r requirements.txt


▶ 2.2 Iniciar servidor Backend
uvicorn main:app --reload


Backend disponible en:
👉 http://127.0.0.1:8000

Documentación automática:
👉 http://127.0.0.1:8000/docs

🌐 3. Instalar y correr el Frontend
📁 Navegar:
cd ../frontend

📦 Instalar dependencias:
npm install

▶ Iniciar servidor de desarrollo:
npm run dev


Frontend disponible en:
👉 http://localhost:5173

📁 4. Estructura del proyecto
Proyecto_G3_Gestion_de_pedidos/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   ├── database.py
│   ├── create_tables.py
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── pages/
│   │   └── components/
│   ├── package.json
│   └── vite.config.js
│
└── README.md

🔧 5. Comandos Git recomendados
Subir cambios:
git add .
git commit -m "Descripción del cambio"
git push origin main

📤 6. Cómo usar la aplicación
1️⃣ En el frontend → Página “Importar Pedidos”

Selecciona un archivo Excel

Presiona Subir Excel

Se muestra la lista actualizada de pedidos

Colores indican estado (confirmado, sin stock, pendiente, etc.)

2️⃣ Backend procesa automáticamente:

Inserta pedidos

Limpia datos nulos

Valida estructura del archivo

🧩 7. Endpoints principales
Método	Ruta	Descripción
POST	/pedidos/importar-excel	Subir Excel de pedidos
GET	/pedidos	Listar pedidos
POST	/stock/importar-excel	Subir stock
POST	/distritos/importar-excel	Subir distritos
