from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from tempfile import gettempdir

from backend.core.database import get_db
from backend.services.inventario_service import exportar_a_excel, clasificar_todos

router = APIRouter()


@router.get("/resumen")
def resumen_inventario(db: Session = Depends(get_db)):
    """Resumen general del inventario con métricas clave."""
    productos = clasificar_todos(db)
    total = len(productos)
    agotados = sum(1 for p in productos if p["estado"] == "agotado")
    bajos = sum(1 for p in productos if p["estado"] == "bajo")
    normales = sum(1 for p in productos if p["estado"] == "normal")
    valor_total = sum(p["valor_total"] for p in productos)

    return {
        "total_productos": total,
        "agotados": agotados,
        "stock_bajo": bajos,
        "normales": normales,
        "valor_total_inventario": round(valor_total, 2),
    }


@router.get("/exportar-excel")
def exportar_excel(db: Session = Depends(get_db)):
    ruta = f"{gettempdir()}\\reporte_sipu.xlsx"
    exportar_a_excel(db, ruta_salida=ruta)
    return FileResponse(
        ruta,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="reporte_sipu.xlsx"
    )
