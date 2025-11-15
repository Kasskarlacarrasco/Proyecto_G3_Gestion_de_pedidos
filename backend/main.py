# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.api import pedidos, stock, distritos, procesos

# Crear tablas en la BD si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gestión de Pedidos")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(pedidos.router)
app.include_router(stock.router)
app.include_router(distritos.router)
app.include_router(procesos.router)

@app.get("/")
def read_root():
    return {"message": "API de Gestión de Pedidos funcionando"}
