import pandas as pd

def cargar_datos(ruta):
    # Eliminamos duplicados exactos y filas incompletas.
    return pd.read_csv(ruta).drop_duplicates().dropna().copy()

def resumen(datos, grupos):
    # Numero de lecturas, incidencias y proporcion.
    return datos.groupby(grupos)['incidencia_proxima_hora'].agg(['count', 'sum', 'mean'])
def dividir(datos):
    return datos[datos.turno < 4].copy(), datos[datos.turno == 4].copy()

def seleccionar(historico, evaluacion):
    seleccion = []
    for maquina, grupo in historico.groupby('maquina'):
        actual = evaluacion[evaluacion.maquina == maquina].copy()
        # Referencias calculadas exclusivamente con el historico de esa maquina.
        actual['motivo'] = ''
        for variable in ['vibracion_mm_s','temperatura_c','presion_bar']:
            media = grupo[variable].mean()
            desviacion = grupo[variable].std()
            fuera = abs(actual[variable] - media) > 2 * desviacion
            actual.loc[fuera, 'motivo'] += variable + '; '
        seleccion.append(actual[actual.motivo != ''])
    return pd.concat(seleccion)
