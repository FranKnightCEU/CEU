def inventario_global(norte, sur):
    inventario = norte.copy()

    for producto, unidades in sur.items():
        inventario[producto] = inventario.get(producto, 0) + unidades

    return dict(sorted(inventario.items()))


if __name__ == "__main__":
    norte = {"raton": 8, "teclado": 5, "monitor": 2}
    sur = {"raton": 4, "webcam": 7, "monitor": 3}
    print(inventario_global(norte, sur))
