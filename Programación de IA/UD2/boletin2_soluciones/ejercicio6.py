def contar_dominios(correos):
    dominios = {}

    for correo in correos:
        if correo.count("@") != 1:
            continue

        usuario, dominio = correo.split("@")
        usuario = usuario.strip()
        dominio = dominio.strip().lower()

        if not usuario or not dominio:
            continue

        dominios[dominio] = dominios.get(dominio, 0) + 1

    return dominios


if __name__ == "__main__":
    correos = [
        "ana@gmail.com", "luis@outlook.com", "marta@GMAIL.com",
        "invalido", "@dominio.com", "usuario@", "otro@gmail.com",
    ]
    print(contar_dominios(correos))
