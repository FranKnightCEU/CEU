def validar_edad(valor):
    try:
        edad = int(valor.strip())
    except (ValueError, AttributeError):
        return None

    if 0 <= edad <= 120:
        return edad
    return None


if __name__ == "__main__":
    valores = ["25", " 41 ", "-3", "abc", "121"]
    print([validar_edad(valor) for valor in valores])
