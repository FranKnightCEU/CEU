# Ejercicio 5

## Contexto

Los datos se encuentran en el fichero **centro_fp_monitorizacion.csv**

Algunos docentes han comunicado sensación de aire cargado y cansancio en determinadas clases. La dirección sospecha que la concentración de CO₂ podría ser demasiado alta cuando las aulas están ocupadas, pero no sabe si ocurre en todas por igual ni en qué franjas.

Se considera que una lectura de **CO₂ superior a 1.000ppm** requiere atención, y que superar **1.200ppm** es especialmente preocupante. Estos valores son umbrales de trabajo de este caso simulado, no un diagnóstico sanitario.

## Lo que tienes que hacer

1. ¿Existen diferencias relevantes de calidad del aire entre las tres aulas? Identifica cuál priorizarías.
2. ¿Los problemas están distribuidos a lo largo del día o se concentran en determinados horarios?
3. ¿Qué relación observas entre la ocupación del aula y el nivel de CO₂? ¿La relación basta para explicar todas las lecturas altas?
4. ¿Hay problemas de calidad de datos que puedan alterar las conclusiones? Explica cómo los has tratado.
5. ¿Qué acciones concretas recomendarías a la dirección y cómo verificarías que funcionan?

## Entrega

- actividad.py o .ipynb
- alertas_aire.json
- Gráficas que consideres necesarias en formato jpg
- Informe de conclusiones > actividad.md o actividad.ipynb

---

# Ejercicio 6

## Contexto

Los datos se encuentran en el fichero **centro_fp_monitorizacion.csv**

La dirección quiere reducir el gasto eléctrico sin perjudicar las clases. El departamento de mantenimiento sospecha que parte de la energía se consume cuando ya no hay alumnos, pero no dispone de un informe que permita decidir dónde intervenir.

Para este estudio, el precio hipotético de la energía es **0,20€/kWh**. Se considera una situación que merece revisión cuando un aula sin alumnos registra **más de 1,8 kWh durante una hora**. Recuerda que consumo registrado no significa automáticamente consumo evitable.

## Lo que tienes que hacer

1. ¿Cuál de las tres aulas consume más energía en el periodo analizado? ¿Qué gasto económico representa?
2. ¿Qué diferencias existen entre las horas con clase y las horas sin alumnos? No te limites a presentar el total: compara también cantidades apropiadas para que la diferencia en número de horas no distorsione la interpretación.
3. ¿Dónde se observan registros poco razonables para aulas vacías? ¿Son hechos aislados o repetidos?
4. ¿En qué medida la temperatura y la ocupación podrían estar relacionadas con el consumo? Busca evidencias.
5. ¿Qué ahorro podríamos justificar con los datos y qué no podemos estimar todavía? Propón un plan de comprobación.

## Entrega

- actividad.py o .ipynb
- revision_energia.json
- Gráficas que consideres necesarias en formato jpg
- Informe de conclusiones > actividad.md o actividad.ipynb

---

# Ejercicio 7

## Contexto

Los datos se encuentran en el fichero **centro_fp_monitorizacion.csv**

Profesores y estudiantes indican que la conexión Wi-Fi se corta y algunas aplicaciones tardan demasiado en responder. El servicio técnico cree que quizá se conectan demasiados dispositivos simultáneamente, aunque también es posible que haya problemas específicos de un aula.

En esta actividad se considera una situación problemática cuando se registran **4 o más desconexiones en una hora** o la latencia supera los **100 ms**. Se trata de criterios internos para este caso.

## Lo que tienes que hacer

1. ¿Se comporta la red de forma parecida en las tres aulas? ¿Dónde concentrarías la primera revisión?
2. ¿Los problemas se repiten en algún horario? ¿Qué evidencias tienes?
3. ¿Tener más dispositivos conectados implica necesariamente más desconexiones o más latencia? Justifica con datos y gráficos.
4. ¿Existen incidencias de latencia sin muchas desconexiones, o desconexiones abundantes con latencia no elevada?
5. ¿Qué hipótesis propones, cuáles no puedes confirmar todavía y qué comprobarías en los equipos de red?

## Entrega

- actividad.py o .ipynb
- incidencias_wifi.json
- Gráficas que consideres necesarias en formato jpg
- Informe de conclusiones > actividad.md o actividad.ipynb
