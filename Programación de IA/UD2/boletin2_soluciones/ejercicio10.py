import json
from pathlib import Path


def cargar_contactos(archivo="contactos.json"):
    ruta = Path(archivo)
    if not ruta.exists():
        return []

    with ruta.open("r", encoding="utf-8") as fichero:
        return json.load(fichero)


def anadir_contacto(nombre, telefono, archivo="contactos.json"):
    contactos = cargar_contactos(archivo)

    if any(contacto["nombre"].casefold() == nombre.casefold() for contacto in contactos):
        return False

    contactos.append({"nombre": nombre, "telefono": telefono})

    with open(archivo, "w", encoding="utf-8") as fichero:
        json.dump(contactos, fichero, ensure_ascii=False, indent=4)

    return True


def buscar_contacto(nombre, archivo="contactos.json"):
    contactos = cargar_contactos(archivo)

    for contacto in contactos:
        if contacto["nombre"].casefold() == nombre.casefold():
            return contacto

    return None


if __name__ == "__main__":
    archivo_prueba = "contactos.json"
    print("Añadido:", anadir_contacto("Ana", "600123123", archivo_prueba))
    print("Duplicado:", anadir_contacto("ANA", "600999999", archivo_prueba))
    print("Búsqueda:", buscar_contacto("ana", archivo_prueba))
