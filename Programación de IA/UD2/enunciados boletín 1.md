# Boletín 1 | Unidad 2

## Ejercicio 1

Desarrolla un programa que solicite una contraseña y compruebe si cumple los siguientes requisitos:
- Tener al menos 8 caracteres.
- Contener al menos una letra mayúscula.
- Contener al menos una letra minúscula.
- Contener al menos un número.
- Contener al menos un carácter especial.

El programa debe indicar si la contraseña es válida y, en caso contrario, mostrar qué requisitos incumple (pueden ser varios de los mencionados simultáneamente).

NOTA: isupper(), islower(), isdigit(), isalnum() son métodos que se pueden aplicar sobre cadenas de caracteres para validar.

---

## Ejercicio 2

Un servidor registra el tiempo de respuesta de sus últimas peticiones HTTP, expresado en milisegundos.

Desarrolla un programa que, a partir de una lista de tiempos, muestre:
- Tiempo medio de respuesta.
- Tiempo máximo y mínimo.
- Número de peticiones que superan los 500 ms. Vamos a considerar que entonces son rápidas y las que sean igual o menor son lentas.
- Porcentaje de peticiones lentas.
- Si el tiempo medio supera los 300 ms, mostrar una alerta de rendimiento.

Usa por ejemplo estos valores de tiempos: 120, 340, 560, 230, 890, 120, 450, 670, 210 y 180

---

## Ejercicio 3

Desarrolla un programa que reciba un texto y muestre las palabras que aparecen más de una vez (TODAS ELLAS), indicando cuántas veces se repite cada una.

La comparación debe ignorar mayúsculas y minúsculas.

**Ejemplo**

- Entrada: Python es un lenguaje muy potente, además Python tiene una sintaxis muy sencilla
- Salida: 
    ```python
    python: 2
    muy: 2
    ```

---

## Ejercicio 4

Una tienda dispone de un inventario con el nombre de cada producto y su cantidad disponible.

Desarrolla un programa que permita:
1. Consultar las existencias de un producto.
2. Añadir unidades a un producto.
3. Retirar unidades de un producto.
4. Mostrar todos los productos.
5. Salir del programa.

No se deben permitir cantidades negativas ni retirar más unidades de las disponibles.

Usa por ejemplo los siguientes datos de inventario:
- teclado: 10,
- ratón: 15,
- monitor: 5

---

## Ejercicio 5

Desarrolla un programa que reciba una dirección IPv4 y determine si tiene un formato válido.

Una dirección IPv4 válida contiene cuatro números enteros entre 0 y 255, separados por puntos.

**Ejemplos**
192.168.1.10 -> Válida
256.10.10.1 -> No válida
192.168.1 -> No válida
192.abc.1.5 -> No válida

---

## Ejercicio 6

Un sistema de soporte técnico recibe incidencias con una prioridad numérica entre 1 y 5.

Desarrolla un programa que, a partir de una lista de incidencias, genere un resumen con:
- Número total de incidencias.
- Cantidad de incidencias por prioridad.
- Prioridad más frecuente.
- Porcentaje de incidencias críticas (prioridad 5).

Usa de ejemplo estas incidencias recibidas (los siguientes valores son las prioridades de estas): 1, 3, 5, 2, 5, 3, 4, 5, 1, 3, 5 y 2

---

## Ejercicio 7

Una tienda online aplica descuentos según el importe de la compra:
| Importe | Descuento |
| ------- | :-------: |
| Menos de 50€ | 0 % |
| Desde 50€ hasta menos de 100€ | 5 % |
| Desde 100€ hasta menos de 200€ | 10 % |
| Desde 200€ | 15 % |

Desarrolla un programa que procese una lista de compras y muestre el importe original, el descuento aplicado y el precio final de cada compra.

Al finalizar, debe mostrar el dinero total descontado de todas las compras que se han hecho.

De ejemplo puedes tomar estas compras:
- Primera compra: 25
- Segunda compra: 75
- Tercera compra: 120
- Cuarta compra: 250
- Quinta compra: 90
- Sexta compra: 350

---

## Ejercicio 8

Un servidor almacena sus accesos mediante cadenas con el siguiente formato:

IP;MÉTODO;CÓDIGO_HTTP

Desarrolla un programa que procese una lista de registros y muestre:
- Número total de peticiones.
- Cantidad de peticiones GET y POST.
- Número de respuestas con error (códigos HTTP mayor o igual que 400).
- Dirección IP que ha realizado más peticiones.

Trata, por ejemplo, los siguientes registros:
- 192.168.1.10;GET;200
- 192.168.1.20;POST;201
- 192.168.1.10;GET;404
- 192.168.1.30;GET;500
- 192.168.1.10;POST;200
- 192.168.1.20;GET;200

---

## Ejercicio 9

Un sistema de monitorización registra periódicamente la temperatura de una máquina.

Desarrolla un programa que identifique los valores anómalos, considerando anómala cualquier temperatura que se aleje más de 15 grados de la media de todas las mediciones.

El programa debe mostrar la media, los valores anómalos y sus posiciones originales.

Ejemplo de temperaturas: 42, 43, 41, 45, 44, 89, 43, 42, 10 y 44

---

## Ejercicio 10

Una plataforma de vídeos tecnologícos registra las categorías de los vídeos que ha visto cada usuario.

Desarrolla un programa que recomiende vídeos de la categoría que más ha consumido el usuario.

No deben recomendarse vídeos que el usuario ya haya visto.

**Ejemplo**
De los siguientes vídeos:
! Nombre del vídeo | Categoría |
| ---------------- | :-------: |
| Python básico | programacion |
| Funciones Python | programacion |
| Docker desde cero | sistemas |
| POO en Python | programacion |
| Listas Python | programacion |
| Redes TCP/IP | sistemas |
| Diccionarios | programacion |
| Linux básico | sistemas |

Puedes suponer que un usuario ha visto "Python básico", "Docker desde cero", "Listas Python" y "Linux básico"