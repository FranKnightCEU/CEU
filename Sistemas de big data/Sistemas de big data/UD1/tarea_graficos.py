# Importamos las librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Eje temporal
tiempo = np.linspace(0, 60, 601) ## 601 puntos de 0 a 60 minutos
momento_accidente = 25

# Potencias
potencia_normal = 80 + 2 * np.sin(tiempo / 4)

potencia_accidente = np.where(
    tiempo < momento_accidente,
    potencia_normal,
    80 + 70 * (1 - np.exp(-(tiempo - momento_accidente) / 12))
)

# Temperaturas
temperatura_normal = 280 + 3 * np.sin(tiempo / 5)
temperatura_accidente = np.where(tiempo < momento_accidente, temperatura_normal, 280 + 620 * (1 - np.exp(-(tiempo - momento_accidente) / 12)))

# Refrigeración
refrigeracion_normal = 100 + 1.5 * np.sin(tiempo / 6)
refrigeracion_accidente = np.where(tiempo < momento_accidente, refrigeracion_normal, 10 + 90 * np.exp(-(tiempo - momento_accidente) / 12))
# Limitar los valores entre 0 y 100
refrigeracion_normal = np.clip(refrigeracion_normal, 0, 100)
refrigeracion_accidente = np.clip(refrigeracion_accidente, 0, 100)


# Mostrar resultados
print("\n--- REFRIGERACION ---")
print("Refrigeracion inicial:", refrigeracion_normal[0])
print("Refrigeracion final normal:", refrigeracion_normal[-1])
print("Refrigeracion final accidentada:", refrigeracion_accidente[-1])