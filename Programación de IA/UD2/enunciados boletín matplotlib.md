# Boletín de ejercicios con matplotlib

Vamos a utilizar en todos los ejercicios el csv subido a Blackboard con datos de sensores industriales ("sensores_industriales.csv") como nuestro dataset para estas actividades.

## Ejercicio 1

Realiza lo siguiente:
- Muestra las cinco primeras filas
- Muestra las tres ultimas filas de datos
- ¿Cuál es la dimensión del dataset?
- Indica los nombres de las columnas del dataset.
- Indica cuántas filas y columnas tiene.

---

## Ejercicio 2

Empecemos con la EDA. Realiza lo siguiente:
- Comprueba los tipos de datos del dataset
- ¿Hay valores ausentes por columna? Indica cuántas.
- Averigua cuántas filas completas estan duplicadas.

---

## Ejercicio 3

Muestra los siguiente datos del dataset:
- El valor medio de consumo
- La temperatura mínima
- La humedad máxima
NOTA: todos los valores debes mostrarlos redondeados a dos decimales.

---

## Ejercicio 4

Realiza:
- Cuenta los registros de cada estado
- Enumera el número de registros de cada zona.
- ¿Cuántas zonas hay diferentes?
- ¿Cuántos sensores tienen un nombre diferente?

---

## Ejercicio 5

Muestra las lecturas de senrores que estén en estado Alerta y cuya temperatura supere los 55 grados. Estos datos mostrados deben ser la fecha, el nombre del sensor, la temperatura y el consumo.
¿Cuántos registros hay en esa muestra?

---

## Ejercicio 6.

Representa la temperatura del sensor S01 durante sus lecturas, ordenadas por fecha. Incluye marcadores, título, etiquetas, cuadrícula y leyenda.

---

## Ejercicio 7

Cuenta cuantas lecturas en estado Alerta hay por zona. Representa el resultado mediante barras con el valor encima de cada una de ellas, empleando las etiquetas de ejes y titulo. Asegúrate que se ven bien los valores representados y en caso contrario usa xlim() o ylim().

---

## Ejercicio 8

Construye un histograma de temperatura con 8 intervalos. Añade titulo, etiquetas y cuadricula horizontal (añade algo de transparencia).

---

## Ejercicio 9

Representa temperatura frente a consumo. Descarta aquellas filas que no tengan consumo o temperatura. Calcula una recta de regresion, dibújala y muestra su ecuación. Luego haz una estimación de cómo sería el consumo para una temperatura de 50 °C a partir de esa expresión matemática.

---

## Ejercicio 10

Representa mediante un histograma la distribución de temperaturas registradas por los sensores. Añade un título, etiquetas de ejes, etc. y guarda el gráfico en formato png antes de mostrarlo.