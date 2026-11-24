# Práctica con Ollama | Primeros pasos

## Descarga y ejecución

```bash
# Levantar el docker de ollama
docker compose up -d
# Descargar el modelo sencillo qwen3 4b
docker exec ollama ollama pull qwen3:4b
# Probarlo
docker exec -it ollama ollama run qwen3:4b

# Descargar qwen3 4b sin razonamiento
docker exec ollama ollama pull qwen3:4b-instruct
```

## Pequeña integración con Python

```python
import requests

url = "http://localhost:11434/api/generate"

datos = {
    "model": "qwen3:4b",
    "prompt": "Cuánto es 1 más 2",
    "stream": False
}

respuesta = requests.post(url, json=datos)

print(respuesta.json()["response"])
```