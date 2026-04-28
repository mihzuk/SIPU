from datetime import datetime, timedelta

from backend.core.database import Base, SessionLocal, engine
from backend.models.models import Alerta, CategoriaEnum, Movimiento, Producto, TipoMovimientoEnum
from backend.services.inventario_service import detectar_alertas_stock, detectar_poca_rotacion


def crear_tablas():
    Base.metadata.create_all(bind=engine)


def _productos_demo():
    return [
        {
            "nombre": "Laptop Lenovo IdeaPad 3",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Portatil de entrada para oficina y estudio.",
            "precio": 2350000,
            "stock": 2,
            "stock_minimo": 5,
            "unidad": "unidad",
        },
        {
            "nombre": "Laptop HP 15",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Portatil de uso general.",
            "precio": 2890000,
            "stock": 8,
            "stock_minimo": 5,
            "unidad": "unidad",
        },
        {
            "nombre": 'Monitor LG 24"',
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Monitor para escritorio.",
            "precio": 790000,
            "stock": 1,
            "stock_minimo": 4,
            "unidad": "unidad",
        },
        {
            "nombre": 'Monitor Samsung 27"',
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Monitor de alta resolucion.",
            "precio": 1180000,
            "stock": 0,
            "stock_minimo": 4,
            "unidad": "unidad",
        },
        {
            "nombre": "Teclado mecanico",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Teclado con retroiluminacion.",
            "precio": 220000,
            "stock": 4,
            "stock_minimo": 10,
            "unidad": "unidad",
        },
        {
            "nombre": "Mouse inalambrico",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Mouse optico para oficina.",
            "precio": 85000,
            "stock": 25,
            "stock_minimo": 8,
            "unidad": "unidad",
        },
        {
            "nombre": "Audifonos Bluetooth",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Audifonos con microfono.",
            "precio": 165000,
            "stock": 3,
            "stock_minimo": 10,
            "unidad": "unidad",
        },
        {
            "nombre": "Parlante portatil",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Bocina recargable con Bluetooth.",
            "precio": 135000,
            "stock": 0,
            "stock_minimo": 6,
            "unidad": "unidad",
        },
        {
            "nombre": "Memoria USB 32 GB",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Unidad flash para transporte de archivos.",
            "precio": 28000,
            "stock": 40,
            "stock_minimo": 15,
            "unidad": "unidad",
        },
        {
            "nombre": "SSD 480 GB",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Disco solido interno.",
            "precio": 185000,
            "stock": 6,
            "stock_minimo": 8,
            "unidad": "unidad",
        },
        {
            "nombre": "SSD 1 TB",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Disco solido de mayor capacidad.",
            "precio": 340000,
            "stock": 12,
            "stock_minimo": 6,
            "unidad": "unidad",
        },
        {
            "nombre": "Router TP-Link",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Router para red domestica.",
            "precio": 210000,
            "stock": 2,
            "stock_minimo": 5,
            "unidad": "unidad",
        },
        {
            "nombre": "Cable HDMI 2 m",
            "categoria": CategoriaEnum.herramientas,
            "descripcion": "Cable de video y audio.",
            "precio": 35000,
            "stock": 60,
            "stock_minimo": 20,
            "unidad": "unidad",
        },
        {
            "nombre": "Cargador USB-C 65W",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Cargador de carga rapida.",
            "precio": 98000,
            "stock": 5,
            "stock_minimo": 10,
            "unidad": "unidad",
        },
        {
            "nombre": "Adaptador Bluetooth",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Adaptador USB para audio.",
            "precio": 42000,
            "stock": 18,
            "stock_minimo": 8,
            "unidad": "unidad",
        },
        {
            "nombre": "Webcam Full HD",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Camara para videollamadas.",
            "precio": 149000,
            "stock": 1,
            "stock_minimo": 5,
            "unidad": "unidad",
        },
        {
            "nombre": "Impresora Epson EcoTank",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Impresora de tanque recargable.",
            "precio": 890000,
            "stock": 0,
            "stock_minimo": 3,
            "unidad": "unidad",
        },
        {
            "nombre": "Regleta 6 tomas",
            "categoria": CategoriaEnum.herramientas,
            "descripcion": "Protector multiple de energia.",
            "precio": 59000,
            "stock": 14,
            "stock_minimo": 10,
            "unidad": "unidad",
        },
        {
            "nombre": "Base refrigerante",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Base para portatil con ventilacion.",
            "precio": 87000,
            "stock": 4,
            "stock_minimo": 6,
            "unidad": "unidad",
        },
        {
            "nombre": "Smartwatch X1",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Reloj inteligente de uso personal.",
            "precio": 245000,
            "stock": 7,
            "stock_minimo": 5,
            "unidad": "unidad",
        },
        {
            "nombre": "Camara de seguridad",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Camara IP para vigilancia.",
            "precio": 175000,
            "stock": 2,
            "stock_minimo": 4,
            "unidad": "unidad",
        },
        {
            "nombre": "Soporte para monitor",
            "categoria": CategoriaEnum.herramientas,
            "descripcion": "Brazo articulado para monitor.",
            "precio": 128000,
            "stock": 9,
            "stock_minimo": 3,
            "unidad": "unidad",
        },
        {
            "nombre": "Cable de red 10 m",
            "categoria": CategoriaEnum.herramientas,
            "descripcion": "Patch cord para red LAN.",
            "precio": 26000,
            "stock": 50,
            "stock_minimo": 20,
            "unidad": "unidad",
        },
        {
            "nombre": "Consola portatil",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Consola de videojuegos compacta.",
            "precio": 980000,
            "stock": 0,
            "stock_minimo": 2,
            "unidad": "unidad",
        },
        {
            "nombre": "Bateria externa 20000 mAh",
            "categoria": CategoriaEnum.electronica,
            "descripcion": "Power bank para dispositivos moviles.",
            "precio": 92000,
            "stock": 11,
            "stock_minimo": 6,
            "unidad": "unidad",
        },
    ]


def seed_demo_data():
    db = SessionLocal()
    try:
        total_esperado = len(_productos_demo())
        total_actual = db.query(Producto).count()

        if total_actual not in (0, total_esperado):
            db.query(Alerta).delete(synchronize_session=False)
            db.query(Movimiento).delete(synchronize_session=False)
            db.query(Producto).delete(synchronize_session=False)
            db.commit()

        if db.query(Producto).count() == total_esperado:
            return False

        db.add_all(Producto(**item) for item in _productos_demo())
        db.commit()

        productos_por_nombre = {producto.nombre: producto for producto in db.query(Producto).all()}
        hoy = datetime.utcnow()
        movimientos_demo = [
            ("Laptop Lenovo IdeaPad 3", 90),
            ("Monitor LG 24\"", 75),
            ("Teclado mecanico", 60),
            ("Audifonos Bluetooth", 120),
            ("Router TP-Link", 45),
            ("Camara de seguridad", 80),
            ("Base refrigerante", 110),
            ("Cargador USB-C 65W", 95),
        ]

        for nombre, dias in movimientos_demo:
            producto = productos_por_nombre[nombre]
            db.add(
                Movimiento(
                    producto_id=producto.id,
                    tipo=TipoMovimientoEnum.ajuste,
                    cantidad=producto.stock,
                    stock_anterior=producto.stock,
                    stock_nuevo=producto.stock,
                    nota="Carga inicial de demostracion",
                    creado_en=hoy - timedelta(days=dias),
                )
            )

        db.commit()
        detectar_alertas_stock(db)
        detectar_poca_rotacion(db, dias_limite=30)
        db.commit()
        return True
    finally:
        db.close()


def bootstrap_database():
    crear_tablas()
    return seed_demo_data()