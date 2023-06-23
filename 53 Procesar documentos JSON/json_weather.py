# Clima
# Obtener la descripción, temperatura máxima y mínima

import json
from urllib.request import Request, urlopen

url = Request("http://globalmentoring.com.mx/api/clima.json")
url.add_header(
    "User-Agent",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15"
)

request = urlopen(url)
body = request.read()

json_response = json.loads(body.decode("utf-8"))
print(f"JSON response: {json_response}")

description = json_response["clima"][0]["descripcion"]
temp_min = json_response["principal"]["temp_min"]
temp_max = json_response["principal"]["temp_max"]

print(f"Descripción: {description}, Temp Min: {temp_min}, Temp Max: {temp_max}")
