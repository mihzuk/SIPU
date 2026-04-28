from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.bootstrap import bootstrap_database
from backend.routers import alertas, movimientos, productos, reportes

app = FastAPI(
    title="SIPU Inventario",
    description="Modulo funcional de inventario con algoritmos de clasificacion, alertas y rotacion.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(productos.router, prefix="/api/productos", tags=["Productos"])
app.include_router(movimientos.router, prefix="/api/movimientos", tags=["Movimientos"])
app.include_router(alertas.router, prefix="/api/alertas", tags=["Alertas"])
app.include_router(reportes.router, prefix="/api/reportes", tags=["Reportes"])


@app.on_event("startup")
def preparar_base_datos():
    bootstrap_database()


@app.get("/")
def root():
    return {"message": "SIPU API activa", "version": "1.0.0"}
