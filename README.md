
# Pipeline de Automatizacion - S.I.P.U (Sistema de Inventario Productivo Universal)
 
## 1. Contexto organizacional 
# Que problema de negocio resuelve este pipeline? 

El pipeline resuelve el problema de la mala calidad de datos en la gestion de inventarios en pequeños y medianos negocios. Muchos negocios manejan sus productos en Excel o de forma manual, lo que genera errores como productos duplicados, precios mal escritos o cantidades incorrectas.

Esto hace que el negocio tenga desorden en su inventario y tome decisiones equivocadas.

# Que decisiones serian incorrectas sin datos limpios? 

Sin datos limpios se pueden tomar decisiones como:
- Comprar productos que no se necesitan  
- Pensar que hay stock cuando en realidad no hay  
- Calcular mal las ganancias  
- Generar alertas equivocadas  

------------------------------------
 
## 2. Resultados sobre Tienda Conecta 
# Filas antes de limpiar vs. despues 

Filas antes de limpiar: (completar con tu dataset)  
Filas despues de limpiar: (completar con tu dataset)  

# Respuestas a las 3 preguntas de negocio (con numeros) 

1. Datos del emprendimiento:

Se manejan datos como:
- nombre_producto  
- precio_unitario  
- cantidad_stock  
- fecha_movimiento  
- categoria_producto  

Ejemplo de problemas en los datos:
- 10% de productos duplicados  
- 15% de precios en formato incorrecto  
- 8% de fechas mal registradas  

---

2. Errores mas probables:

- precio_unitario incorrecto → afecta el dinero del negocio  
- cantidad_stock incorrecta → genera errores en inventario  
- fecha_movimiento incorrecta → afecta analisis y predicciones  

---

3. Funcion agregada al pipeline:
   
```python
def validar_alertas_stock_y_rotacion(dataframe, stock_minimo, dias_sin_venta):
 ```

## 3. Decisiones de diseno del pipeline 

Para cada funcion: que hace y por que existe 

- limpiar_estructura(): elimina filas completamente vacias y registros incompletos.  
  Sin esto, el dataset tendria informacion basura que no aporta nada.  

- limpiar_texto(): corrige nombres de productos y categorias (minusculas, sin espacios extra).  
  Sin esto, un mismo producto podria aparecer varias veces con nombres diferentes.  

- eliminar_duplicados(): elimina productos repetidos.  
  Sin esto, el inventario estaria inflado con registros duplicados.  

- convertir_precios(): convierte el precio a formato numerico.  
  Sin esto, no se pueden hacer calculos de ventas correctamente.  

- validar_stock(): revisa que la cantidad de productos no sea negativa ni vacia.  
  Sin esto, el inventario no reflejaria la realidad del negocio.  

- limpiar_fechas(): estandariza el formato de fechas.  
  Sin esto, los analisis de ventas y predicciones fallarian.  

---

## 4. Conexion con SIPU 

Respuestas a las 3 preguntas organizacionales 

1. Que datos usa SIPU?  
SIPU usa datos de productos, inventario, precios y movimientos de ventas.  

2. Que pasa si los datos estan mal?  
- El sistema puede mostrar informacion incorrecta  
- Se generan alertas equivocadas  
- Se toman malas decisiones  
- Se pueden generar perdidas economicas  

3. Como ayuda el pipeline?  
- Limpia y organiza los datos  
- Mejora la calidad de la informacion  
- Permite que el sistema funcione correctamente  
- Hace que las alertas y analisis sean confiables  

---

## 5. Como ejecutar 

Instrucciones para correr el pipeline desde cero 

1. Tener instalado Python  
2. Instalar la libreria pandas (pip install pandas)  
3. Tener el archivo Excel con los datos  
4. Ejecutar el script del pipeline  

Ejemplo:

```python
import pandas as pd

# cargar datos
df = pd.read_excel("datos_inventario.xlsx")

# aplicar limpieza
df = limpiar_datos(df)

# guardar resultados
df.to_excel("datos_limpios.xlsx", index=False)
```
