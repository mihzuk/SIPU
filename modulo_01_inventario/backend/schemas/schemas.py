"""Schemas Pydantic para validación de datos de entrada/salida."""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ProductoCreate(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=200)
    categoria: str
    descripcion: Optional[str] = None
    precio: float = Field(..., ge=0)
    stock: int = Field(default=0, ge=0)
    stock_minimo: int = Field(default=10, ge=0)
    unidad: str = "unidad"


class ProductoOut(BaseModel):
    id: int
    nombre: str
    categoria: str
    precio: float
    stock: int
    stock_minimo: int
    unidad: str
    creado_en: Optional[datetime]

    class Config:
        from_attributes = True


class MovimientoCreate(BaseModel):
    producto_id: int
    tipo: str = Field(..., pattern="^(entrada|salida|ajuste)$")
    cantidad: int = Field(..., gt=0)
    nota: Optional[str] = ""


class MovimientoOut(BaseModel):
    id: int
    producto_id: int
    tipo: str
    cantidad: int
    stock_anterior: int
    stock_nuevo: int
    nota: Optional[str]
    creado_en: Optional[datetime]

    class Config:
        from_attributes = True
