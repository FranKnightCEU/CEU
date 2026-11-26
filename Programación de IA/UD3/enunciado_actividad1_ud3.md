# Actividad 1

## Contexto del problema

Un servicio de soporte recibe incidencias de distintos sistemas. Los responsables necesitan clasificar automáticamente los nuevos tickets en **prioridad 0 (baja), 1 (media) o 2 (alta)**. El histórico que se adjunta en el csv (actividad1.csv) ya incluye una prioridad asignada por técnicos.

## Datos disponibles

El fichero con los datos recibidos es actividad1.csv. Os explico por encima las distintas columnas que tiene y lo que representan sus valores:

| Columna | Significado |
|---|---|
| `ticket` | Identificador del ticket |
| `tiempo_respuesta_min` | Minutos hasta la primera respuesta |
| `usuarios_afectados` | Usuarios afectados |
| `servicios_afectados` | Servicios afectados |
| `errores_ultima_hora` | Errores registrados recientemente |
| `impacto_declarado` | Evaluación inicial: 0, 1 o 2 |
| `prioridad_real` | Prioridad histórica: 0, 1 o 2 |

## Qué se pide

Usando el modelo DecisionTreeClassifier de scikit-learn con las cinco características del csv, entrena el modelo con esos datos (por ejemplo reserva 2l 25% para evaluar el modelo con test_size=0.25).

1. ¿Es bueno tu modelo entrenado para predecir? ¿En qué prioridades se equivoca más?
2. ¿Qué pasaría si una incidencia de prioridad alta se clasificara como baja? ¿Deberíamos fijarnos únicamente en el porcentaje global de aciertos?
3. Prepara cuatro tickets nuevos con condiciones claramente diferentes y obtén la prioridad estimada para cada uno. Intenta probar casos que consideres válidos y otros tantos que no lo son.
4. De todos los registros, guarda los que te aparezcan con prioridad urgente en un fichero json. Realiza las predicciones que consideres oportunas.
5. Genera y guarda un par de gráficos que sean representativos del comportamiento del modelo y sus predicciones de la prioridad de los tickets.