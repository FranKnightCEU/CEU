def medias_superiores(lecturas):
    temperaturas = {}

    for sensor, temperatura in lecturas:
        temperaturas.setdefault(sensor, []).append(temperatura)

    medias = {
        sensor: sum(valores) / len(valores)
        for sensor, valores in temperaturas.items()
    }

    return sorted(
        ((sensor, media) for sensor, media in medias.items() if media > 50),
        key=lambda elemento: elemento[1],
        reverse=True,
    )


if __name__ == "__main__":
    lecturas = [
        ("S1", 48), ("S1", 54), ("S2", 62),
        ("S2", 66), ("S3", 45), ("S3", 51),
    ]
    for sensor, media in medias_superiores(lecturas):
        print(f"{sensor}: {media:.2f} °C")
