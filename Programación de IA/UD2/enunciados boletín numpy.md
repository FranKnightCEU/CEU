# Boletín de ejercicios solo de numpy

## Ejercicio 1

Una aplicación de inteligencia artificial analiza imágenes para identificar objetos. Después de procesar varias imágenes, devuelve las siguientes puntuaciones de confianza:

[0.95, 0.82, 0.91, 0.65, 0.98, 0.73]

Desarrolla un programa utilizando que:
- Muestre el número total de predicciones realizadas.
- Calcule la confianza media, máxima y mínima.
- Muestre todas las confianzas expresadas en porcentaje.
- Muestre las confianzas superiores o iguales a 0.90.
- Indique cuántas predicciones tienen una confianza inferior a 0.80.

---

## Ejercicio 2

Una empresa industrial utiliza sensores para controlar la temperatura de diferentes máquinas. Los datos recogidos son los siguientes:

[42, 58, 63, 39, 75, 51, 46, 82, 55, 34]

La empresa establece los siguientes criterios:
- Temperatura normal: inferior a 50 °C.
- Temperatura elevada: entre 50 y 69 °C, ambos incluidos.
- Temperatura crítica: 70 °C o superior.

Desarrolla un programa utilizando que:
- Obtenga las temperaturas elevadas.
- Obtenga las temperaturas críticas.
- Muestre los índices de los sensores con temperatura crítica.
- Genere un nuevo array con las etiquetas "Normal", "Elevada" o "Crítica" según corresponda.
- Calcule la temperatura media de los sensores cuya temperatura sea superior o igual a 50 °C.
- Muestre cuántos sensores tienen una temperatura normal.

---

## Ejercicio 3

Una empresa tecnológica dispone de cuatro servidores que ejecutan diferentes aplicaciones de inteligencia artificial.

Durante tres intervalos de tiempo se ha registrado su porcentaje de utilización de CPU:

Servidor 1: [35, 42, 38]
Servidor 2: [75, 82, 79]
Servidor 3: [45, 55, 50]
Servidor 4: [90, 95, 88]

Cada columna corresponde a una medición.

Desarrolla un programa utilizando NumPy que:
- Muestre las dimensiones, forma y número total de elementos de la matriz.
- Calcule el consumo medio de cada servidor.
- Calcule el consumo medio de todos los servidores en cada intervalo.
- Obtenga el consumo máximo registrado.
- Identifique los servidores cuyo consumo medio sea superior a 70%
- Muestre los índices de esos servidores.
- Calcule la desviación estándar del consumo de cada servidor.

---

## Ejercicio 4

Una aplicación recibe las mediciones de temperatura de varios sensores.

Durante la transmisión se han producido algunos errores, generando valores negativos que deben corregirse.

Las lecturas recibidas son: [45, 52, -10, 61, 48, -5, 55, 72, 43, 59, 64, 50]

La aplicación debe preparar los datos para que posteriormente puedan ser utilizados por un sistema de inteligencia artificial.

Desarrolla un programa utilizando NumPy que:
- Cree una copia independiente del array original.
- Sustituya todos los valores negativos por cero.
- Compruebe que el array original no ha sido modificado.
- Reorganice los datos corregidos en una matriz de 3 filas y 4 columnas.
- Calcule la media de cada fila.
- Obtenga la matriz transpuesta.
- Convierta la matriz transpuesta en un vector de una dimensión.
- Añada al final del vector las siguientes mediciones nuevas: [60, 65, 70].

---

## Ejercicio 5

Una empresa ha desarrollado un sistema de inteligencia artificial para detectar defectos en productos industriales.

Cada producto es analizado por tres modelos diferentes. Cada modelo devuelve un valor de confianza comprendido entre 0 y 1, que representa su confianza en que el producto es defectuoso.

Se han analizado ocho productos, obteniendo las siguientes predicciones:

[0.92, 0.88, 0.95]
[0.45, 0.52, 0.48]
[0.85, 0.91, 0.89]
[0.30, 0.25, 0.35]
[0.78, 0.82, 0.80]
[0.96, 0.94, 0.98]
[0.55, 0.62, 0.58]
[0.89, 0.93, 0.91]

Cada fila representa un producto y cada columna representa un modelo.

Para decidir si un producto debe ser revisado, la empresa utiliza los siguientes criterios:
- Si la confianza media de los tres modelos es superior o igual a 0.90, el producto se clasifica como "Revisión urgente".
- Si la confianza media es superior o igual a 0.70 e inferior a 0.90, se clasifica como "Revisión".
- Si la confianza media es inferior a 0.70, se clasifica como "Correcto".

Desarrolla un programa utilizando NumPy que:
- Muestre el número de productos y el número de modelos utilizados.
- Calcule la confianza media de cada producto.
- Calcule la confianza media de cada modelo.
- Obtenga la confianza máxima y mínima registrada.
- Clasifique cada producto según los criterios establecidos.
- Muestre los índices de los productos que necesitan revisión urgente.
- Calcule cuántos productos pertenecen a cada categoría.
- Calcule la desviación estándar de las predicciones de cada producto.
- Identifique los productos cuya desviación estándar sea superior a 0.04, indicando que existe cierta discrepancia entre los modelos.
- Genere una nueva matriz con las confianzas expresadas en porcentaje y redondeadas a dos decimales.
- Añada las siguientes predicciones de un noveno producto y vuelva a calcular las medias por producto: [0.91, 0.87, 0.94]