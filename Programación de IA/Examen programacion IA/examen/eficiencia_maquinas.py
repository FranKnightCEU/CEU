import pandas as pd

def cargar_datos(ruta):
    # Eliminamos duplicados exactos y filas incompletas.
    return pd.read_csv(ruta).drop_duplicates().dropna().copy()

def resumen(datos, grupos):
    # Numero de lecturas, incidencias y proporcion.
    return datos.groupby(grupos)['incidencia_proxima_hora'].agg(['count', 'sum', 'mean'])
def preparar(datos):
    datos = datos[datos.carga_pct > 0].copy()
    datos['indicador'] = datos.consumo_kwh / datos.carga_pct
    return datos

def consumo_por_grupo(datos, grupos):
    return datos.groupby(grupos)[['consumo_kwh','carga_pct','indicador']].mean()

def seleccionar(datos):
    return datos[datos.indicador >= 0.13].copy()
