# Boletín de ejercicios solo de pandas

## Ejercicio 1

Una empresa tecnológica utiliza cinco servidores para ejecutar diferentes aplicaciones de IA.

Se ha registrado el porcentaje de memoria RAM utilizada por cada servidor:

| Servidor | RAM utilizada (%) |
| :------: | :---------------: |
| servidor1	| 45 |
| servidor2	| 78 |
| servidor3	| 92 |
| servidor4	| 63 |
| servidor5	| 85 |

Realiza:

- Crea una Series con los porcentajes de RAM, utilizando los nombres de los servidores como índices.
- Muestra todos los valores.
- Muestra el porcentaje de RAM del servidor3 mediante loc.
- Muestra el porcentaje del segundo servidor mediante iloc.
- Calcula la media de utilización de RAM.
- Muestra el valor máximo y el mínimo.
- Muestra el número total de servidores.

---

## Ejercicio 2

Una aplicación de IA recibe información de varios sensores industriales.

Los datos registrados son:
| Sensor | Temperatura | Humedad
| :----: | :---------: | :-----: |
| S01 | 42.5 | 65 |
| S02 | 58.3 | 48 |
| S03 | 71.8 | 35 |
| S04 | 49.2 | 60 |
| S05 | 63.7 | 42 |
| S06 | 38.9 | 70 |

Desarrolla un programa que realice las siguientes operaciones:
- Crea un DataFrame con los datos anteriores.
- Muestra el número de filas y columnas.
- Muestra únicamente las columnas sensor y temperatura.
- Muestra los sensores cuya temperatura sea superior a 50 grados.
- Muestra los sensores cuya temperatura sea superior a 50 grados y cuya humedad sea inferior a 50.
- Muestra los sensores cuya temperatura esté comprendida entre 40 y 60 grados, ambos incluidos.
- Añade una columna denominada alerta que contenga True si la temperatura supera los 60 grados y False en caso contrario.

---

## Ejercicio 3

Una aplicación de reconocimiento de imágenes almacena los resultados de diferentes predicciones realizadas por un modelo de IA.

Se dispone del siguiente archivo predicciones.csv.

Desarrolla un programa que realice las siguientes operaciones:
- Importa el CSV utilizando Pandas, teniendo en cuenta el separador de campos (coma) y el separador decimal (coma).
- Muestra las tres primeras filas del DataFrame.
- Muestra la información de las columnas y sus tipos de datos.
- Selecciona únicamente las predicciones de las categorías gato y perro, utilizando isin().
- Selecciona las predicciones cuya confianza sea superior a 0.90.
- Cambia el nombre de la columna confianza por probabilidad.
- Redondea los valores de probabilidad a dos decimales.
- Exporta el resultado a un nuevo archivo denominado predicciones_procesadas.csv, sin incluir los índices.

---

## Ejercicio 4

Una empresa está comparando los resultados obtenidos por diferentes modelos de IA.

Los datos iniciales son:

[
    {"modelo": "Modelo_A", "precision": 0.8543, "estado": "activo"},
    {"modelo": "Modelo_B", "precision": 0.9231, "estado": "activo"},
    {"modelo": "Modelo_C", "precision": 0.7645, "estado": "pruebas"},
    {"modelo": "Modelo_D", "precision": 0.9756, "estado": "activo"},
    {"modelo": "Modelo_E", "precision": 0.8812, "estado": "pruebas"}
]

Realiza lo siguiente:
- Crea un DataFrame a partir de la lista de diccionarios.
- Muestra los dos últimos registros.
- Muestra únicamente la primera fila mediante iloc.
- Muestra el valor de precisión del tercer modelo mediante loc.
- Sustituye el estado pruebas por evaluación, utilizando replace().
- Añade una nueva columna denominada aprobado, que indique si la precisión es igual o superior a 0.90.
- Selecciona los modelos activos cuya precisión sea superior a 0.90 utilizando query().
- Redondea la precisión a tres decimales.
- Exporta el resultado a un archivo JSON, donde cada registro sea un objeto independiente, con una indentación de cuatro espacios.

---

## Ejercicio 5

Una empresa está desarrollando un sistema de monitorización de dispositivos inteligentes mediante IA.

Los dispositivos registran información sobre su temperatura, utilización de CPU y estado operativo.

La empresa dispone de la siguiente información:

| Dispositivo | Temperatura | CPU (%) | Estado |
| :---------: | :---------: | :-----: | :----: |
| DEV01 | 45.5 | 62 | operativo |
| DEV02 | 72.3 | 89 | operativo |
| DEV03 | 38.7 | 45 | mantenimiento |
| DEV04 | 81.2 | 95 | operativo |
| DEV05 | 56.8 | 71 | operativo |
| DEV06 | 69.4 | 84 | mantenimiento |
| DEV07 | 43.1 | 55 | operativo |
| DEV08 | 77.6 | 92 | operativo |

Se pide desarrollar un programa que realice las siguientes operaciones:

Parte A. Creación y exploración de datos
1. Crea un DataFrame utilizando una lista de diccionarios.
2. Muestra sus dimensiones, tipos de datos y las cinco primeras filas.
3. Calcula la temperatura media y el porcentaje máximo de CPU.

Parte B. Filtrado de dispositivos
4. Selecciona los dispositivos que estén operativos y tengan una temperatura superior a 70 grados.
5. Selecciona los dispositivos cuya CPU esté comprendida entre el 60 % y el 90 %.
6. Selecciona los dispositivos cuya temperatura supere los 75 grados o cuya CPU supere el 90 %.

Parte C. Transformación de datos
7. Añade una columna denominada alerta_temperatura, cuyo valor sea True si la temperatura supera los 70 grados.
8. Añade una columna denominada alerta_cpu, cuyo valor sea True si la CPU supera el 85 %.
9. Añade una columna denominada alerta_general que sea True cuando exista una alerta de temperatura o de CPU.
10. Sustituye el estado mantenimiento por revisión.
11. Renombra la columna cpu como uso_cpu.

Parte D. Exportación e importación
12. Exporta todos los datos procesados a un archivo CSV denominado dispositivos_procesados.csv.
13. Exporta únicamente los dispositivos que tengan una alerta general activa a un archivo JSON denominado dispositivos_alerta.json.
14. Exporta los datos procesados a un archivo Excel denominado dispositivos.xlsx, utilizando el nombre de hoja Monitorizacion.
15. Importa nuevamente el archivo Excel con Pandas y muestra sus tres primeras filas.

Parte E. Base de datos SQLite
16. Crea una base de datos SQLite denominada dispositivos.db.
17. Crea una tabla denominada dispositivos con los campos dispositivo, temperatura, cpu y estado.
18. Inserta al menos cuatro registros de los datos originales.
29. Utilizando pd.read_sql_query(), recupera los dispositivos cuya temperatura supere los 60 grados.
20. Muestra los resultados y cierra la conexión.