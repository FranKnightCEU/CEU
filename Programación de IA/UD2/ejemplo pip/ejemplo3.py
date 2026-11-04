dni = "12345678x"

longitud = len(dni)
print(longitud)


numero_dni = dni[0:8]
letra_dni = dni[8]

print(dni)
print(numero_dni)
print(letra_dni)

print(dir(dni)) # Dir nos indica todas las posibles acciones de un comando.


mi_lista = ["uno", "dos", "tres"]

for i in mi_lista:
    print(i)

for i in range(0,34):
    print(i)

for i in dni:
    print(i)


#int("a")   Salta error


try: 
    nuevo_valor = int("texto")

except ValueError as error:
    print("Dato no válido")
    print(f"Código de error: {error}")

