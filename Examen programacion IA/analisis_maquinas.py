import pandas as pd
def obtener_datos_csv(fichero):
    return pd.read_csv(fichero)

def limpiar_nulos_duplicados(datos_brutos):
    return datos_brutos.drop_duplicates().dropna()

def insertar_datos(datos,maquina):
    info = datos[datos["maquina"] == maquina]
    return {
        "maquina": maquina,
        "registros": len(info),
        "media_temperatura": round(info["temperatura_c"].mean(),2),
        "media_vibracion": round(info["vibracion_mm_s"].mean(),2),
        "media_consumo": round(info["consumo_kwh"].mean(),2),
        "media_presion": round(info["presion_bar"].mean(),2),
        "incidencias": info["incidencia_proxima_hora"].sum(),
        "porcentaje_incidencias": info["incidencia_proxima_hora"].sum()*100/len(info)
    }