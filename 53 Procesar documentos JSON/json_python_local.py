import json

# Ruta al archivo JSON local
path = "53 Procesar documentos JSON/JSON/test_json.json"
# Leer el archivo JSON local
with open(path, "r") as file:
    json_data = json.load(file)

# Procesar el contenido del archivo JSON
# Imprimir solo los nombres de las personas
[print(f"Persona: {person['nombre']}, {person['edad']}") for person in json_data["personas"]]

# Acceder a otras variables del JSON si es necesario
print(f"\nTotal de personas: {json_data['total']}")
print(f"Mensaje: {json_data['mensaje']}")
