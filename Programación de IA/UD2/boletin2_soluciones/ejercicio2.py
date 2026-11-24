def calcular_pedido(lineas):
    total_pedido = 0

    for linea in lineas:
        producto = linea["producto"]
        precio = linea["precio"]
        unidades = linea["unidades"]

        if precio < 0 or unidades <= 0:
            print(f"Línea rechazada ({producto}): precio o unidades no válidos.")
            continue

        importe = precio * unidades
        total_pedido += importe
        print(f"{producto}: {importe:.2f} €")

    print(f"Total del pedido: {total_pedido:.2f} €")
    return total_pedido


if __name__ == "__main__":
    pedido = [
        {"producto": "SSD", "precio": 69.90, "unidades": 2},
        {"producto": "RAM", "precio": 45, "unidades": 3},
        {"producto": "Cable", "precio": -4, "unidades": 1},
    ]
    calcular_pedido(pedido)
