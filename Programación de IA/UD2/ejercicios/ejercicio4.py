'''
## Ejercicio 4

Una empresa inmobiliaria está desarrollando un modelo de Inteligencia Artificial para estimar el precio de las viviendas a partir de sus características.

Para probar el funcionamiento de una futura aplicación, necesita un programa que permita introducir las características de una vivienda y calcular una primera estimación simplificada de su precio.

La empresa utiliza los siguientes parámetros:
- Precio base por metro cuadrado: 1.800 €
- Incremento por cada habitación: 5.000 €
- Incremento por disponer de garaje: 12.000 €
- Incremento por disponer de ascensor: 8.000 €

Crea un programa que:
- Defina las constantes adecuadas para los precios establecidos.
- Solicite al usuario la superficie de la vivienda en metros cuadrados.
- Solicite el número de habitaciones.
- Pregunte si dispone de garaje (si/no).
- Pregunte si dispone de ascensor (si/no).
- Convierta los datos introducidos a los tipos adecuados.
- Calcule el precio estimado de la vivienda teniendo en cuenta la superficie, las habitaciones y las características adicionales.
- Muestre un informe con las características de la vivienda y el precio estimado, utilizando f-strings y mostrando el resultado con dos decimales.

'''

PrecioBasePorMetro = 1800
IncrementoHabitacion = 5000
IncrementoGarage = 12000
IncrementoAscensor = 8000

# Solicitar al usuairo la sup en metros
SuperficieUsuario = float(input("Introduzca la superficie en m^2 que tiene su vivienda: "))

# Solicitar al usuairo la cantidad de habitaciones
HabitacionesUsuario = int(input("Introduzca la cantidad de habitaciones que tiene su vivienda: "))

# Pregunta garaje
Salir = False
while Salir == False:
    respuesta = input("Tiene un garaje en su vivienda? (SI/NO): ")
    if respuesta.lower() == "si" :
        respuestaGarage = True 
        Salir = True
    elif respuesta.lower() == "no":
        respuestaGarage = False 
        Salir = True
    else:
        print("Por favor, introduzca un valor válido, Si o No")

if respuestaGarage == True:
    print("Tiene garaje")
else:
    print("No tiene garaje")

#Pregunta ascensor
Salir2 = False
while Salir2 == False:
    respuesta2 = input("Tiene un ascensor en su vivienda? (SI/NO): ")
    if respuesta2.lower() == "si" :
        respuestaAscensor = True 
        Salir2 = True
    elif respuesta2.lower() == "no":
        respuestaAscensor = False 
        Salir2 = True
    else:
        print("Por favor, introduzca un valor válido, Si o No")

if respuestaAscensor == True:
    print("Tiene Ascensor")
else:
    print("No tiene Ascensor")

PrecioBonuses = 0

if respuestaGarage == True:
    PrecioBonuses += IncrementoGarage
if respuestaAscensor == True:
    PrecioBonuses += IncrementoAscensor

PrecioMetros = SuperficieUsuario * PrecioBasePorMetro
PrecioHabitaciones = HabitacionesUsuario * IncrementoHabitacion

PrecioTotal = PrecioBonuses + PrecioMetros + PrecioHabitaciones


print(f"El precio total asciende a {PrecioTotal:.2f}€")
print(f"Precio por cada metro cuadrado: {PrecioBasePorMetro}€")
print(f"Precio por metros cuadrados en total: {PrecioMetros}€")
print(f"Precio por habitaciones: {IncrementoHabitacion}€")
print(f"Precio por las habitaciones en total: {PrecioHabitaciones}€")
print(f"Precio por ascensor: {IncrementoAscensor}€")
print(f"Precio por garaje: {IncrementoGarage}€")