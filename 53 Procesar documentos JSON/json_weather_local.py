# Extracción de info desde JSON en local
# Extraer descripción, temp min y max

import json

path = "53 Procesar documentos JSON/JSON/test_weather.json"

with open(path, 'r') as file:
    json_data = json.load(file)

description = json_data["clima"][0]["descripcion"]
temp_min = json_data["principal"]["temp_min"]
temp_max = json_data["principal"]["temp_max"]

print(f"Descripción: {description}, Temp Min: {temp_min}, Temp Max: {temp_max}")
