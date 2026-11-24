from collections import Counter


def resumir_accesos(archivo_entrada="accesos.txt", archivo_salida="resumen.txt"):
    with open(archivo_entrada, "r", encoding="utf-8") as archivo:
        ips = [linea.strip() for linea in archivo if linea.strip()]

    recuento = Counter(ips)

    with open(archivo_salida, "w", encoding="utf-8") as archivo:
        for ip, cantidad in sorted(recuento.items()):
            archivo.write(f"{ip}: {cantidad}\\n")

    return recuento


if __name__ == "__main__":
    resultado = resumir_accesos()
    print("Resumen guardado en resumen.txt")
    print(dict(resultado))
