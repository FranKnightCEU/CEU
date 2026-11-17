# Ejercicio 8

## Contexto

Formas parte de un equipo que está preparando los datos de una futura herramienta de **mantenimiento predictivo**. Una fábrica utiliza tres máquinas industriales (M01, M02 y M03) y ha facilitado un histórico de medidas. Cada registro contiene las condiciones de funcionamiento y una columna que indica si **se observó una incidencia durante la hora siguiente**.

El responsable quiere saber **qué máquina necesita atención prioritaria, qué variables podrían ayudar a anticipar problemas y qué registros convendría revisar antes de entrenar un modelo de IA**. No te pide entrenar un modelo todavía.

Los datos se encuentran en el fichero **lecturas_maquinas.csv**

Explicación de las columnas:

| Columna | Significado |
|---|---|
| registro | Identificador único esperado de cada lectura |
| maquina | M01, M02 o M03 |
| turno | Turno de trabajo, de 1 a 4 |
| franja | Franja de observación, de 0 a 9 dentro de cada turno |
| carga_pct | Porcentaje de carga de la máquina |
| temperatura_c | Temperatura en °C |
| vibracion_mm_s | Vibración en mm/s |
| consumo_kwh | Consumo de energía de la franja |
| presion_bar | Presión en bares |
| incidencia_proxima_hora | 1 si se registró una incidencia en la siguiente hora; 0 en caso contrario |

**Advertencia:** son datos simulados de un histórico y pueden contener errores de calidad. La columna de incidencia describe lo ocurrido *después* de la lectura.

## Lo que tienes que hacer

Elabora un análisis que permita comunicar a mantenimiento:

1. ¿Hasta qué punto son fiables los datos recibidos para comenzar a analizarlos? ¿Qué decisiones has tomado ante los problemas que encuentres? NOTA: para borrar datos duplicados puedes usar el método drop_duplicates() y para borrar filas con columnas None puedes hacer uso de dropna().
2. ¿Cuál de las tres máquinas parece más preocupante? Explica en qué evidencias te basas y por qué no basta con elegir la máquina que tenga una medida máxima más alta. NOTA: sería bueno saber el valor medio de cada parámetro, cuántas incidencias se registan y el porcentaje de estas de cada máquina.
3. ¿Qué señales previas a una incidencia merece la pena investigar? ¿Qué relación observas entre las medidas disponibles y las incidencias registradas? NOTA: un diagrama de dispersión te puede ayudar a identificar patrones de comportamiento seleccionando adecuadamente los parámetros.
4. Selecciona **un conjunto reducido de lecturas que merecerían una revisión preventiva**, aunque todavía no haya ocurrido una incidencia. Explica tus criterios sin consultar la etiqueta de incidencia para decidir qué lecturas seleccionas. NOTA: elige unos criterios o valores a partir de los cuáles considerar que hay un funcionamiento anómalo.
5. Comprueba cuántas de las lecturas que marcaste como aviso acabaron teniendo una incidencia y cuántas no. ¿Es suficiente esta comprobación para asegurar que tu sistema anticipará averías futuras? NOTA: Compara los registros que tienen incidencia y cuáles marcaste tú como con incidencia. 

Elige **al menos dos representaciones gráficas diferentes** que aporten información útil al diagnóstico. No hay un único análisis correcto; se valorarán las decisiones y las conclusiones respaldadas por datos.

## Entrega

- Crea un archivo **analisis_maquinas.py** con **al menos tres funciones propias**: una para cargar o preparar datos, una para obtener resultados de un subconjunto y otra para seleccionar registros de interés mediante criterios definidos por ti. Puedes añadir más si lo necesitas.
- Crea un **actividad.ipynb** que **importe y utilice** esas funciones. No se considera válido copiar todas las funciones en las celdas del notebook sin importarlas desde el .py.
- En el notebook incluye el análisis, las gráficas y una conclusión final.
- Exporta **lecturas_revision.json** con las lecturas seleccionadas para revisión y guarda las gráficas en formato jpg.

---

# Ejercicio 9

## Contexto

Formas parte del equipo de análisis de datos de una fábrica que utiliza tres máquinas industriales (M01, M02 y M03). El coste de la energía ha aumentado y la dirección sospecha que **algunas máquinas están consumiendo más de lo razonable para el trabajo que realizan**.

Antes de comprar nuevos equipos, quieren comprobar si los datos históricos permiten encontrar diferencias de eficiencia. El análisis servirá para proponer una revisión técnica, no para demostrar por sí solo que una máquina está averiada.

Los datos se encuentran en el fichero **lecturas_maquinas.csv**.

Explicación de las columnas:

| Columna | Significado |
|---|---|
| registro | Identificador de la lectura |
| maquina | M01, M02 o M03 |
| turno | Turno de trabajo, de 1 a 4 |
| franja | Franja de observación, de 0 a 9 dentro del turno |
| carga_pct | Carga de trabajo de la máquina en porcentaje |
| temperatura_c | Temperatura en °C |
| vibracion_mm_s | Vibración en mm/s |
| consumo_kwh | Energía consumida en la franja, en kWh |
| presion_bar | Presión en bares |
| incidencia_proxima_hora | 1 si hubo incidencia en la siguiente hora, 0 si no |

**Advertencia:** el histórico puede contener duplicados y valores ausentes. No confundas una lectura de consumo elevada con un uso ineficiente: también podría deberse a que la máquina está trabajando con mayor carga. Los registros corresponden a franjas de medición comparables.

## Lo que tienes que hacer

Elabora un informe para el responsable de producción que responda a lo siguiente:

1. ¿Se pueden comparar directamente todos los registros? ¿Has detectado problemas de calidad que puedan distorsionar el diagnóstico? NOTA: puedes usar drop_duplicates() y dropna().
2. ¿Qué máquina o máquinas merecen una revisión de su **eficiencia energética**? Aporta evidencias teniendo en cuenta **tanto el consumo como el trabajo realizado**. NOTA: puedes crear un indicador propio que relacione consumo_kwh con carga_pct, y debes explicar sus limitaciones.
3. ¿Cambia tu diagnóstico si estudias los diferentes turnos? ¿Hay momentos que resulten especialmente interesantes? NOTA: puedes comparar subconjuntos mediante filtros y construir gráficas de barras o líneas.
4. Selecciona **un conjunto reducido de lecturas para revisión de consumo**, utilizando criterios que tú definas. Justifica por qué son llamativas y qué información adicional pedirías al equipo de mantenimiento. NOTA: evita seleccionar únicamente por consumo máximo.
5. ¿Qué relación parece haber entre el consumo, la carga y las otras medidas disponibles? ¿Puedes concluir que la causa del posible gasto excesivo es una avería? Razona la respuesta.

Elige **al menos dos representaciones gráficas diferentes**, que permitan responder a preguntas concretas. Se valorarán los resultados razonados, no el número de cálculos realizados.

## Entrega

- Crea un archivo **eficiencia_maquinas.py** con **al menos tres funciones propias**: una para cargar o preparar los datos, otra para analizar subconjuntos y otra para seleccionar registros de revisión. Puedes incorporar funciones adicionales.
- Crea un archivo **actividad_9.ipynb** que **importe y utilice** las funciones del .py. No copies su implementación en el notebook.
- Incluye en el notebook el análisis, las gráficas y conclusiones explicadas.
- Exporta **revision_energetica.json** y guarda las gráficas en formato jpg.

---

# Ejercicio 10

## Contexto

La misma fábrica quiere iniciar un proyecto de **IA para anticipar incidencias**, pero antes de entrenar modelos necesita comprobar si dispone de datos apropiados y si el comportamiento que se observa en los registros más recientes se parece al de los anteriores.

El equipo técnico propone utilizar las lecturas de los **turnos 1, 2 y 3 como histórico de desarrollo** y reservar el **turno 4 para una comprobación posterior**. Esto permite estudiar si los patrones aprendidos de un periodo anterior serían representativos del siguiente.

No tienes que entrenar ningún modelo. Tu trabajo consiste en **preparar, comparar y auditar el conjunto de datos** para que el equipo de IA conozca sus limitaciones.

Los datos se encuentran en el fichero **lecturas_maquinas.csv** y contienen las siguientes columnas:

| Columna | Significado |
|---|---|
| registro | Identificador de la lectura |
| maquina | M01, M02 o M03 |
| turno | Turno de 1 a 4 |
| franja | Franja de observación de 0 a 9 |
| carga_pct | Porcentaje de carga de trabajo |
| temperatura_c | Temperatura en °C |
| vibracion_mm_s | Vibración en mm/s |
| consumo_kwh | Consumo de energía por franja |
| presion_bar | Presión en bares |
| incidencia_proxima_hora | Resultado observado durante la hora siguiente (0/1) |

**Advertencia:** los registros pueden contener problemas de calidad. La columna incidencia_proxima_hora representa información posterior a la medición; úsala para estudiar y comprobar resultados, pero no para definir qué lecturas parecen anómalas en el momento en que se tomaron.

## Lo que tienes que hacer

Prepara un informe para el equipo que desarrollará la futura IA:

1. ¿Qué fiabilidad tienen los datos de partida? ¿Cuántos registros utilizables quedan después del tratamiento que consideres adecuado? NOTA: dispones de drop_duplicates() y dropna().
2. ¿El histórico de los turnos 1–3 y los datos del turno 4 tienen **la misma distribución de incidencias** en las tres máquinas? Explica dónde hay diferencias importantes y por qué podrían afectar a un futuro sistema de IA. NOTA: no basta con contar incidencias; compara proporciones y ten presente el número de registros.
3. ¿Detectas cambios en las mediciones de vibración, presión o temperatura entre ambos periodos? Selecciona las variables que mejor permitan justificar tus conclusiones y represéntalas gráficamente. NOTA: puedes utilizar dispersión, barras o histogramas.
4. Selecciona **lecturas del turno 4 que merezcan una auditoría adicional** por presentar condiciones poco habituales respecto al histórico de la **misma máquina**. Explica tu criterio sin utilizar incidencia_proxima_hora para seleccionar esas lecturas. NOTA: puedes comparar con valores de referencia obtenidos de los turnos 1–3.
5. Comprueba, **después de seleccionar**, qué sucedió con las lecturas marcadas y valora las limitaciones del conjunto de datos para entrenar una IA. ¿Qué otra información o más registros pedirías al equipo de producción?

Construye **al menos dos gráficos diferentes** que ayuden a comparar los periodos y a justificar las observaciones.

## Entrega

- Crea **preparacion_ia_maquinas.py** con **al menos tres funciones propias**: carga/preparación, análisis por subconjunto y selección de registros de auditoría. Puedes incluir también una función para dividir por turnos.
- Crea **actividad_10.ipynb** que **importe y utilice** las funciones del .py.
- Debe contener el análisis, al menos dos gráficas diferentes y conclusiones finales.
- Exporta **historico_ia.csv**, **evaluacion_ia.csv** y **lecturas_auditoria.json** y guarda las gráficas en formato jpg.
