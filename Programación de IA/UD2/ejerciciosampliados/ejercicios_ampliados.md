# Ejercicio 1

## Contexto

Trabajas en el departamento de sistemas de una empresa que gestiona una tienda online.

Durante los últimos días, varios clientes han comunicado que la web funciona especialmente lenta en determinados momentos. Algunos aseguran que incluso ha dejado de responder durante unos segundos.

El responsable de infraestructura sospecha que el problema podría estar relacionado con el tráfico recibido, aunque desconoce si existe realmente una relación entre el número de peticiones y el tiempo de respuesta del servidor.

Para realizar una primera investigación, te encarga analizar una simulación del comportamiento del servidor durante 24 horas.

## Datos disponibles

Como todavía no se dispone de un sistema de monitorización completo, tendrás que generar un conjunto de datos simulado. Estas son las características que debes tener en cuenta:

- Periodo de observación: 24 horas, de 0 a 23
- Tráfico habitual: Entre 50 y 100 peticiones por minuto
- Tráfico de 18 a 20h: Aumento adicional de 120 a 180 peticiones por minuto
- Tiempo de respuesta (en ms): 50 + peticiones por minuto × 1.8 + variación aleatoria
- Variación aleatoria: Entre 0 y 40 ms
- Tráfico elevado: Más de 12000 peticiones/hora
- Respuesta lenta: Más de 400 ms

## Lo que tienes que hacer

El responsable técnico necesita un informe que le permita determinar si existe algún problema de rendimiento, cuándo aparece y qué posibles causas deberían investigarse. Debes aportarle el fichero csv de la monitorización (generado aleatoriamente con las condiciones dadas), el fichero json con las incidencias registradas y algunas gráficas en jpg que aporten valor a tu decisión.

El código que desarrolles debe responder a:

1. ¿Se comporta el servidor de manera similar durante todo el día o existen periodos claramente diferentes?

2. ¿Existe alguna relación entre el tráfico recibido y la lentitud de la web?

3. ¿En qué momentos debería centrarse inicialmente la investigación del departamento técnico? Identifica los registros relevantes y explica los criterios utilizados para seleccionarlos.

4. ¿Se producen situaciones de respuesta lenta sin que exista tráfico elevado, o situaciones de tráfico elevado sin respuesta lenta?

5. ¿Podemos afirmar que la web ha sufrido una caída?

## Entrega

- Script en python > actividad.py o actividad.ipynb
- Datos de monitorización generados automáticamente > monitorizacion.csv
- Registros relevantes o incidencias registradas > incidencias.json
- Gráficas que consideres necesarias en formato jpg.
- Informe de conclusiones > actividad.md o actividad.ipynb

Cuanto más expliques lo que haces mejor (comenta tu código, da una visión crítica y constructiva, etc.)

---

# Ejercicio 2

## Contexto

Una explotación agrícola controla dos zonas de un invernadero de tomates. En una de ellas se han observado síntomas de estrés en las plantas. Se desconoce si el motivo puede estar relacionado con la temperatura, la humedad o el funcionamiento de la climatización. El responsable solicita una investigación basada en datos.

## Datos disponibles

Genera **24 mediciones por zona**, una cada hora, con **48 registros** en total.

| Campo | Condición |
|---|---|
| hora | 0 a 23, en cada zona |
| zona | A o B |
| temperatura_c | A: 19–27°C; B: 22–30°C |
| humedad_pct | 40–75% |
| luminosidad_lux | 300–900lux |
| consumo_w | 100 + temperatura_c * 12 + luminosidad_lux * 0.08 + variación |

La variación del consumo será un valor aleatorio entre 0 y 25W. Se considera que una medición necesita revisión cuando la temperatura es **superior a 28°C** o la humedad es **inferior a 45%**.

## Lo que tienes que hacer

1. ¿Las dos zonas presentan condiciones ambientales similares? ¿Cuál te preocupa más?
2. ¿En qué momentos hay condiciones fuera de los límites recomendados? ¿Son incidencias de temperatura, humedad o ambas?
3. ¿Qué información aportan los datos sobre la relación entre temperatura, luminosidad y consumo eléctrico?
4. ¿Qué dos o tres representaciones gráficas ayudarían a explicar los resultados al responsable? Justifica la elección.
5. ¿Puedes concluir que las condiciones medidas son la causa del estrés de las plantas? ¿Qué comprobarías después?

## Entrega

- actividad.py o actividad.ipynb
- invernadero.csv
- alertas_invernadero.json
- Gráficos en jpg
- Conclusiones breves en md o en el notebook

---

# Ejercicio 3

## Contexto

Una empresa de logística observa que algunos envíos llegan con retraso. La dirección cree que podrían influir la distancia, el volumen de paquetes y la lluvia, y quiere reducir los tiempos sin disparar el coste.

## Datos disponibles

Genera **60 repartos**, 20 para cada zona (Centro, Norte y Sur).

| Campo | Condición |
|---|---|
| envío | 1 a 60 |
| zona | Centro, Norte, Sur: 20 repartos por zona |
| distancia_km | 5–50km |
| paquetes | 1–5 |
| lluvia | 0 no; 1 sí. Envíos 21–36 con lluvia |
| tiempo_min | 12 + distancia_km * 1.5 + paquetes * 4 + lluvia * 25 + variación |
| coste_eur | 3 + distancia_km * 0.55 + paquetes * 0.80 + lluvia * 2 |

La variación del tiempo estará entre 0 y 12 minutos. Se considera lenta una entrega que supere **90 minutos** y elevado un coste superior a **30€**.

## Lo que tienes que hacer

1. ¿Qué factores parecen relacionarse con la duración de los repartos?
2. ¿Qué zonas presentan más casos problemáticos? ¿Es suficiente la comparación de medias para decidir cuál funciona peor?
3. ¿Cómo se relacionan lluvia, tiempos y costes? Explica los límites de tus conclusiones.
4. ¿Existen repartos costosos que no sean lentos, o lentos que no sean costosos?
5. ¿Qué repartos investigarías primero y qué recomendarías al responsable?

Elige y justifica las gráficas que resulten útiles.

### Entrega

- actividad.py o .ipynb
- repartos.csv
- repartos_problematicos.json
- Gráficos jpg
- Informe de conclusiones

---

# Ejercicio 4

## Contexto

Un centro de FP monitoriza dos aulas de informática y quiere investigar el aumento del gasto eléctrico. Le preocupa especialmente el consumo fuera del horario lectivo.

## Datos disponibles

Genera una medición por hora de cada aula durante 24 horas (**48 registros**).

| Campo | Condición |
|---|---|
| hora | 0–23 |
| aula | A y B |
| alumnos | 15–30 en horario lectivo; 0 fuera |
| ordenadores | En clase, uno encendido por alumno; fuera, 0–5 |
| temperatura_c | 19–29°C |
| consumo_kwh | 0.8 + ordenadores * 0.12 + climatización + variación |
| coste_eur | consumo_kwh * tarifa |

El horario lectivo es **8:00–14:00, inclusive**. La climatización consume 1,5kWh por hora cuando la temperatura es superior a 25°C, y 0,5kWh por hora en caso contrario. La variación del consumo está entre 0 y 0,4kWh. Tarifa: 0,18€/kWh en clase y 0,12€/kWh fuera de horario. Un posible desperdicio se registra cuando hay **más de 2 ordenadores encendidos fuera de clase**.

## Lo que tienes que hacer

1. ¿Cuál de las dos aulas presenta mayor consumo y gasto diario?
2. ¿Cómo cambia el comportamiento durante el horario lectivo y fuera de él?
3. ¿Qué influencia parecen tener los ordenadores y la temperatura?
4. ¿Dónde se detectan posibles consumos innecesarios? ¿Se puede considerar desperdiciado todo el consumo de esas horas?
5. ¿Coinciden las horas de mayor consumo con las de mayor coste? Justifica.
6. ¿Qué medidas recomendarías y qué datos adicionales necesitarías?

Elige y justifica las gráficas que resulten útiles.

## Entrega

- actividad.py o .ipynb
- consumo_aulas.csv
- desperdicios.json
- Gráficos jpg
- Informe de conclusiones