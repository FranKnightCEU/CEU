def importar_archivo(file):
    datos = pd.read_csv(file, sep=';', decimal=',')
    return datos

def filtrar_datos(datos):
    datos_filtrados = datos.dropna().drop_duplicates()
    return datos_filtrados

def obtener_datos(file):
    
