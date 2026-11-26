import pandas as pd

def cargar_datos(ruta):
    # Eliminamos duplicados exactos y filas incompletas.
    return pd.read_csv(ruta).drop_duplicates().dropna().copy()

def resumen(datos, grupos):
    # Numero de lecturas, incidencias y proporcion.
    return datos.groupby(grupos)['incidencia_proxima_hora'].agg(['count', 'sum', 'mean'])
def seleccionar(datos):
    # Umbrales exploratorios, sin consultar la etiqueta.
    return datos[(datos.vibracion_mm_s >= 6) | (datos.temperatura_c >= 90) | (datos.presion_bar < 6.3)].copy()
