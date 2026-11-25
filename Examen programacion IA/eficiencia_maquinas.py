# Función para analizar los datos recibidos y limpiarlos de nulos y duplicados
def limpiar_datos(datos_brutos):
    num_duplicados = datos_brutos.duplicated().sum()
    num_nulos = datos_brutos.isna().sum().sum()
    datos_limpios = datos_brutos.drop_duplicates().dropna()
    return num_duplicados, num_nulos, datos_limpios

# Función para extrar indicadores y datos del problema planteado sobre consumo energético
def obtener_datos_energeticos(datos,maquina):
    datos_maquina = datos[datos["maquina"] == maquina]
    return {
        "maquina": maquina,
        "num_registros": len(datos_maquina),
        "media_carga": round(datos_maquina["carga_pct"].mean(),2),
        "media_consumo": round(datos_maquina["consumo_kwh"].mean(),2),
        "media_temperatura": round(datos_maquina["temperatura_c"].mean(),2),
        "indicador_carga_consumo": round(datos_maquina["consumo_kwh"].mean()*100/datos_maquina["carga_pct"].mean(),2)
    }