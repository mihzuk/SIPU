from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.core.database import Base
import enum


class CategoriaEnum(str, enum.Enum):
    electronica = "electronica"
    alimentos = "alimentos"
    medicamentos = "medicamentos"
    ropa = "ropa"
    herramientas = "herramientas"
    otros = "otros"


class TipoMovimientoEnum(str, enum.Enum):
    entrada = "entrada"
    salida = "salida"
    ajuste = "ajuste"


class NivelAlertaEnum(str, enum.Enum):
    critico = "critico"
    bajo = "bajo"
    sin_rotacion = "sin_rotacion"
    normal = "normal"


class Producto(Base):
    __tablename__ = "productos"

    id          = Column(Integer, primary_key=True, index=True)
    nombre      = Column(String(200), nullable=False)
    categoria   = Column(Enum(CategoriaEnum), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio      = Column(Float, nullable=False, default=0.0)
    stock       = Column(Integer, nullable=False, default=0)
    stock_minimo = Column(Integer, nullable=False, default=10)
    unidad      = Column(String(50), default="unidad")
    creado_en   = Column(DateTime(timezone=True), server_default=func.now())
    actualizado_en = Column(DateTime(timezone=True), onupdate=func.now())

    movimientos = relationship("Movimiento", back_populates="producto")
    alertas     = relationship("Alerta", back_populates="producto")


class Movimiento(Base):
    __tablename__ = "movimientos"

    id          = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    tipo        = Column(Enum(TipoMovimientoEnum), nullable=False)
    cantidad    = Column(Integer, nullable=False)
    stock_anterior = Column(Integer, nullable=False)
    stock_nuevo    = Column(Integer, nullable=False)
    nota        = Column(Text, nullable=True)
    creado_en   = Column(DateTime(timezone=True), server_default=func.now())

    producto = relationship("Producto", back_populates="movimientos")


class Alerta(Base):
    __tablename__ = "alertas"

    id          = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    nivel       = Column(Enum(NivelAlertaEnum), nullable=False)
    mensaje     = Column(String(500), nullable=False)
    resuelta    = Column(Integer, default=0)  # 0 = activa, 1 = resuelta
    creado_en   = Column(DateTime(timezone=True), server_default=func.now())

    producto = relationship("Producto", back_populates="alertas")
