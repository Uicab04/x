
import openai
import requests

# Tu clave de API de OpenAI va aquí
openai.api_key = "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"

# Establecemos el modelo que queremos utilizar (en este caso, GPT-3)
model_engine = "text-davinci-002"

# Creamos la solicitud a la API de OpenAI
response = openai.Completion.create(
    engine=model_engine,
    prompt="Realiza un mapa conceptual del metodo agil con tres conceptos que son ventajas desventajas y estado actual",
    max_tokens=2048,
    n=1,
    temperature=0.5,
)

# Procesamos la respuesta

response_text = response["choices"][0]["text"]

print(response_text)
