'''
# Ejercicios de la unidad 2

## Ejercicio 1

Una empresa industrial ha desarrollado un modelo de visión artificial para detectar productos defectuosos. Antes de ponerlo en producción, el departamento de IA necesita calcular su rendimiento y comprobar que cumple los requisitos mínimos.

Estos son los datos que sabemos:
- Imágenes evaluadas: 1.200
- Clasificaciones correctas: 1.116
- Confianza de la última predicción: 0.94
- Exactitud mínima exigida: 0.90
- Confianza mínima exigida. 0.85
- Pruebas de seguridad superadas: True
- Modelo activo: True

Crea un programa que:
- Tenga definidas las variables y constantes adecuadas para hacer fácil la lectura del código
- Calcule el número de clasificaciones que están mal.
- Calcule la exactitud del modelo en porcentaje.
- Compruebe que la exactiid alcanza el mínimo exigido.
- Compruebe que la última predicción supera o no el umbral de confianza
- Determine si el modelo se puede poner en producción (exactitud, pruebas de seguridad y modelo activo)
- Determine si la última predicción puede aceptarse automáticamente siempre que el modelo esté autorizado para pro y su confianza alcance el umbral.
- Muestre todos los resultados

'''
# Variables
imagenesEv = 1200 #Evaluaciones totales
ClasificacionesCor = 1116 #Clasificaciones correctas
ConfUltPred = 0.94 #Confianza última predicción
EXMINEXI = 0.9 #Exactitud mínima exigida
CONMINEXI = 0.85 #Confianza mínima exigida
PRUEBASUP = True
MODACT = True 

# Número de clasificaciones erróneas
numclasifmal = imagenesEv - ClasificacionesCor

#Exactitud en porcentaje
Exactitud = 100 - ((numclasifmal*100)/imagenesEv)

#Prints
print(f"Clasificaciones totales: {imagenesEv}")
print(f"Clasificaciones erróneas: {numclasifmal}")
print(f"Exactitud: {Exactitud}")

#Comprobación de la exactitud
if Exactitud < EXMINEXI:
    Comprobacion = False
    print("Exactitud mínima no cumple los requisitos.")
else: 
    Comprobacion = True
    print(f"Exactitud mínima ({EXMINEXI * 100}%) alcanzada.")

#Comprobacion de la confianza
if ConfUltPred > CONMINEXI:
    ConfFin = True
    print(f"El modelo cumple con el parámetro de confianza ({CONMINEXI * 100}%)")
else:
    ConfFin = False
    print(f"El modelo no cumple con el parámetro de confianza ({CONMINEXI *100}%)")
# Evaluación
if PRUEBASUP == True and MODACT == True and Comprobacion == True:
    print("Modelo válido para producción")
    Produccion = True
else:
    print("Modelo no válido para producción")
    Produccion = False

# Evaluación predicciones

if Produccion == True and ConfFin == True:
    print(f"El modelo está capacitado para considerar la última predicción como válida.")
else: 
    print("La última predicción del modelo no debe ser cpnsiderada válida de forma automática.")



