📦 Gestión de Pedidos — FASTAPI + REACT + MYSQL

Proyecto completo para la gestión de pedidos, importación desde Excel, procesamiento, validación de stock, dashboard básico, y panel web en React.

Incluye:

🟦 Backend — FastAPI + SQLAlchemy + MySQL

🟩 Frontend — React + Vite (TypeScript)

🗄 Base de datos — MySQL/MariaDB

📊 Importación de Excel para:

Pedidos

Stock

Distritos

🚀 Instalación y Ejecución
1️⃣ Clonar el repositorio
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO

🛠 Backend (FastAPI)
2️⃣ Entrar a la carpeta backend
cd backend

3️⃣ Crear entorno virtual

Windows:

python -m venv venv
venv\Scripts\activate


Mac/Linux:

python3 -m venv venv
source venv/bin/activate

4️⃣ Instalar dependencias
pip install -r requirements.txt


Si no lo tienes, genera el archivo requirements:

pip freeze > requirements.txt

5️⃣ Configurar base de datos MySQL

Crear una BD llamada:

gestion_pedidos


O el nombre que quieras, pero debe coincidir con tu cadena de conexión.

6️⃣ Configurar variables de entorno

Crear archivo:

backend/.env


Contenido:

MYSQL_USER=root
MYSQL_PASSWORD=TU_PASSWORD
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=gestion_pedidos


⚠️ Cambiar los valores según tu entorno.

7️⃣ Ejecutar migración automática de tablas

FastAPI + SQLAlchemy ya crea las tablas al iniciar (si está activado en tu código):

uvicorn main:app --reload


Backend disponible en:

👉 http://127.0.0.1:8000

👉 Documentación automática: http://127.0.0.1:8000/docs

🎨 Frontend (React + Vite)
8️⃣ Abrir carpeta frontend

Desde la raíz del proyecto:

cd frontend

9️⃣ Instalar dependencias
npm install

🔟 Levantar el servidor de desarrollo
npm run dev


Tu frontend estará en:

👉 http://localhost:5173/

📁 Estructura del proyecto
gestion-pedidos/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── database/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   ├── venv/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.ts
│
└── README.md
