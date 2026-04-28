from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.schemas.schemas import MovimientoCreate
from backend.services.inventario_service import registrar_movimiento
from backend.models.models import Movimiento

router = APIRouter()


@router.get("/")
def listar_movimientos(limit: int = 100, db: Session = Depends(get_db)):
    movs = db.query(Movimiento).order_by(Movimiento.creado_en.desc()).limit(limit).all()
    return [
        {
            "id": m.id,
            "producto": m.producto.nombre if m.producto else "—",
            "tipo": m.tipo.value,
            "cantidad": m.cantidad,
            "stock_anterior": m.stock_anterior,
            "stock_nuevo": m.stock_nuevo,
            "nota": m.nota,
            "fecha": str(m.creado_en),
        }
        for m in movs
    ]


@router.post("/")
def nuevo_movimiento(data: MovimientoCreate, db: Session = Depends(get_db)):
    exito, mensaje, datos = registrar_movimiento(
        db, data.producto_id, data.tipo, data.cantidad, data.nota
    )
    if not exito:
        raise HTTPException(400, mensaje)
    return {"mensaje": mensaje, "datos": datos}
