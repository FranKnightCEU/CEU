# Boletín 2 | Unidad 2

## Ejercicio 1

Una aplicación recibe nombres de usuario con espacios y diferentes combinaciones de mayúsculas. Desarrolla una función que normalice cada nombre (elimina espacios extremos y pasa a minúsculas), descarte los vacíos y devuelva la lista sin duplicados, conservando el orden de primera aparición.

Ejemplo de entrada: `[' Ana ', 'LUIS', 'ana', '  ', 'Luis', 'Marta']`.


---

## Ejercicio 2

Un comercio recibe líneas de pedido como diccionarios con "producto", "precio" y "unidades". Calcula el importe total de cada línea y del pedido completo. Las líneas con precio negativo o unidades no positivas deben rechazarse con un mensaje, sin interrumpir el resto del cálculo.

Prueba por ejemplo para estos datos:
{'producto': 'SSD', 'precio': 69.90, 'unidades': 2},
{'producto': 'RAM', 'precio': 45, 'unidades': 3},
{'producto': 'Cable', 'precio': -4, 'unidades': 1}


---

## Ejercicio 3

Un sistema almacena lecturas "(sensor, temperatura)" de varios dispositivos. Calcula para cada sensor su temperatura media y muestra solo los sensores cuya media supere los 50 grados, ordenados de mayor a menor media.


---

## Ejercicio 4

Un formulario recibe edades introducidas como texto. Crea una función que convierta cada valor a entero y acepte solamente edades entre 0 y 120. Debe devolver "None" si la entrada es inválida.

Prueba la función con "['25', ' 41 ', '-3', 'abc', '121']".


---

## Ejercicio 5

Una plataforma recibe notas de usuarios entre 1 y 5. Elabora un informe con el número de votos de cada puntuación, la media y la puntuación más frecuente. Si varias puntuaciones empatan en frecuencia, muestra todas ellas ordenadas.


---

## Ejercicio 6

Un servicio recibe una lista de direcciones de correo. Agrúpalas por dominio y cuenta cuántas pertenecen a cada uno. Ignora direcciones sin una única "@" o sin texto a ambos lados de ella; la comparación de dominios no distingue mayúsculas.


---

## Ejercicio 7

Dos almacenes guardan sus existencias en diccionarios "{producto: unidades}". Genera un inventario global que sume los productos comunes y conserve los exclusivos de cada almacén. Muestra el resultado ordenado alfabéticamente.

Usa por ejemplo:
- norte = {'raton': 8, 'teclado': 5, 'monitor': 2}
- sur = {'raton': 4, 'webcam': 7, 'monitor': 3}


---

## Ejercicio 8

Un archivo de texto llamado "accesos.txt" contiene una dirección IP por línea. Crea un programa que cuente las apariciones de cada IP, ignore las líneas vacías y escriba en "resumen.txt" las IP y sus cantidades.


---

## Ejercicio 9

Una empresa recibe un CSV "ventas.csv" con columnas "producto", "unidades" y "precio". 

Calcula la facturación acumulada de cada producto y muestra el producto con mayor facturación.


---

## Ejercicio 10

Una agenda guarda contactos en un archivo "contactos.json" como lista de objetos con "nombre" y "telefono".

Desarrolla dos funciones: una para añadir un contacto (sin permitir nombres duplicados ignorando mayúsculas) y otra para buscarlo por nombre.

Prueba ambas funciones.

