from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.models.models import Alerta
from backend.services.inventario_service import detectar_alertas_stock, detectar_poca_rotacion

router = APIRouter()


@router.get("/")
def listar_alertas(db: Session = Depends(get_db)):
    alertas = db.query(Alerta).filter(Alerta.resuelta == 0).order_by(Alerta.creado_en.desc()).all()
    return [
        {
            "id": a.id,
            "producto": a.producto.nombre if a.producto else "—",
            "nivel": a.nivel.value,
            "mensaje": a.mensaje,
            "fecha": str(a.creado_en),
        }
        for a in alertas
    ]


@router.post("/escanear")
def escanear_alertas(db: Session = Depends(get_db)):
    alertas = detectar_alertas_stock(db)
    return {"alertas_generadas": len(alertas), "detalle": alertas}


@router.get("/rotacion")
def alertas_rotacion(dias: int = 30, db: Session = Depends(get_db)):
    return detectar_poca_rotacion(db, dias_limite=dias)


@router.put("/{alerta_id}/resolver")
def resolver_alerta(alerta_id: int, db: Session = Depends(get_db)):
    alerta = db.query(Alerta).filter(Alerta.id == alerta_id).first()
    if not alerta:
        return {"error": "Alerta no encontrada"}
    alerta.resuelta = 1
    db.commit()
    return {"mensaje": "Alerta marcada como resuelta."}
