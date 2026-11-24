import csv
from collections import defaultdict


def facturacion_por_producto(nombre_archivo="ventas.csv"):
    facturacion = defaultdict(float)

    with open(nombre_archivo, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            producto = fila["producto"]
            unidades = int(fila["unidades"])
            precio = float(fila["precio"])
            facturacion[producto] += unidades * precio

    return dict(facturacion)


if __name__ == "__main__":
    facturacion = facturacion_por_producto()
    for producto, total in sorted(facturacion.items()):
        print(f"{producto}: {total:.2f} €")

    if facturacion:
        producto_maximo = max(facturacion, key=facturacion.get)
        print(f"Mayor facturación: {producto_maximo} ({facturacion[producto_maximo]:.2f} €)")
