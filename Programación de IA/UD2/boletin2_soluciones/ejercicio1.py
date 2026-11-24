def normalizar_usuarios(nombres):
    resultado = []
    vistos = set()

    for nombre in nombres:
        normalizado = nombre.strip().lower()
        if normalizado and normalizado not in vistos:
            resultado.append(normalizado)
            vistos.add(normalizado)

    return resultado


if __name__ == "__main__":
    usuarios = [' Ana ', 'LUIS', 'ana', '  ', 'Luis', 'Marta']
    print(normalizar_usuarios(usuarios))
