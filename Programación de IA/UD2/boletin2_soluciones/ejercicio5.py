def informe_puntuaciones(votos):
    if any(not isinstance(voto, int) or not 1 <= voto <= 5 for voto in votos):
        raise ValueError("Todas las puntuaciones deben ser enteros entre 1 y 5.")

    frecuencias = {puntuacion: votos.count(puntuacion) for puntuacion in range(1, 6)}
    media = sum(votos) / len(votos) if votos else None

    if votos:
        frecuencia_maxima = max(frecuencias.values())
        mas_frecuentes = [
            puntuacion
            for puntuacion, cantidad in frecuencias.items()
            if cantidad == frecuencia_maxima
        ]
    else:
        mas_frecuentes = []

    return frecuencias, media, mas_frecuentes


if __name__ == "__main__":
    votos = [5, 4, 5, 3, 4, 2, 5, 4]
    frecuencias, media, mas_frecuentes = informe_puntuaciones(votos)
    print("Votos:", frecuencias)
    print("Media:", media)
    print("Puntuación/es más frecuente/s:", mas_frecuentes)
