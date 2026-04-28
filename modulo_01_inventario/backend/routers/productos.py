from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.models.models import Producto, CategoriaEnum
from backend.schemas.schemas import ProductoCreate, ProductoOut
from backend.services.inventario_service import clasificar_todos

router = APIRouter()


@router.get("/", response_model=list[ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    return db.query(Producto).all()


@router.get("/clasificados")
def listar_clasificados(db: Session = Depends(get_db)):
    return clasificar_todos(db)


@router.post("/", response_model=ProductoOut)
def crear_producto(data: ProductoCreate, db: Session = Depends(get_db)):
    try:
        cat = CategoriaEnum(data.categoria)
    except ValueError:
        raise HTTPException(400, f"Categoría inválida: {data.categoria}")

    nuevo = Producto(
        nombre=data.nombre,
        categoria=cat,
        descripcion=data.descripcion,
        precio=data.precio,
        stock=data.stock,
        stock_minimo=data.stock_minimo,
        unidad=data.unidad,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.get("/{producto_id}", response_model=ProductoOut)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    p = db.query(Producto).filter(Producto.id == producto_id).first()
    if not p:
        raise HTTPException(404, "Producto no encontrado")
    return p


@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    p = db.query(Producto).filter(Producto.id == producto_id).first()
    if not p:
        raise HTTPException(404, "Producto no encontrado")
    db.delete(p)
    db.commit()
    return {"mensaje": f"Producto '{p.nombre}' eliminado correctamente."}
