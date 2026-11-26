import pandas
def abrir_archivo(ruta):
    if ruta.endswith('.csv'):
        datos = pandas.read_csv(ruta)
        return datos
    elif ruta.endswith('.json'):
        datos = pandas.read_json(ruta)
        return datos
    else:
        raise ValueError("Formato de archivo no soportado. Solo se permiten archivos CSV o JSON.")




def limpiar_datos(datos):
    datos = datos.dropna().drop_duplicates()
    return datos