'''
    
## Ejercicio 2

Una empresa de ciberseguridad ha desarrollado un modelo de Inteligencia Artificial para detectar correos electrónicos fraudulentos (phishing). Antes de ponerlo en producción, el departamento de IA necesita evaluar su rendimiento y comprobar que cumple los requisitos mínimos de seguridad.

Estos son los datos que sabemos:
- Correos electrónicos analizados: 2.500
- Correos clasificados correctamente: 2.350
- Correos fraudulentos detectados: 420
- Correos fraudulentos no detectados: 30
- Confianza de la última predicción: 0.91
- Exactitud mínima exigida: 0.92
- Tasa máxima de fraudes no detectados: 0.08
- Confianza mínima para bloquear automáticamente: 0.90
- Sistema de seguridad habilitado: True
- Modelo actualizado: True

Crea un programa que:
- Tenga definidas las variables y constantes adecuadas para hacer fácil la lectura del código.
- Calcule el número de correos clasificados incorrectamente.
- Calcule la exactitud del modelo en porcentaje.
- Calcule la tasa de correos fraudulentos no detectados.
- Compruebe que la exactitud alcanza el mínimo exigido.
- Compruebe que la tasa de fraudes no detectados no supera el máximo permitido.
- Determine si el modelo se puede poner en producción (exactitud, tasa de fraudes no detectados, sistema de seguridad habilitado y modelo actualizado).
- Determine si el último correo, suponiendo que ha sido clasificado como fraudulento, puede bloquearse automáticamente, siempre que el modelo esté autorizado para producción y su confianza alcance el umbral.
- Muestre todos los resultados.

'''
print("EJERCICIO 2")
CorrAna = 2500
CorrClaCor = 2350
CorrClaErr = 420
CorrrFraNoDet = 30
Conf = 0.91
EXACTMINEX = 0.92
TASAMAXFRAUNODET = 0.08
CONFMINPARADETC = 0.90
SISTMSEGHABI = True
MODANALIZ = True


# Correos clasificados incorrectamente
CorrAnalInc = CorrAna - CorrClaCor
print(f"Correos clasificados de forma errónea: {CorrAnalInc}")

# Exactitud en %
Exactitud =((CorrClaCor*100)/CorrAna)
print(f"Exactitud en %: {Exactitud}%")

# Comprobar la exactitud
if Exactitud > CONFMINPARADETC:
    MARGENEXACT = True 
    print(f"El modelo cumple con la exactitud requerida ({CONFMINPARADETC * 100} %)")
else:
    MARGENEXACT = False 
    print(f"El modelo no cumple con la exactitud requerida")

#Calcular la tasa de correos Frau no detectados
TasaFrau = CorrrFraNoDet / CorrAna

# Comprobar que la tasa de fraudes no detectados no supera el máximo permitido
if  TasaFrau > TASAMAXFRAUNODET:
    print(f"Tasa excedida: {TasaFrau} > {TASAMAXFRAUNODET} ")
    FraudesBajoMin = False
else:
    print(f"La tasa cumple con los parámetros: {TasaFrau} < {TASAMAXFRAUNODET}")
    FraudesBajoMin = True

#Comprobar si puede pasar a Prod
if FraudesBajoMin == True and MARGENEXACT == True and SISTMSEGHABI == True and MODANALIZ == True:
    print("El modelo puede psar a aproducción")
else:
    print("El modelo no puede pasar a producción.")