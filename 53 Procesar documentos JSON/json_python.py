# Leer el archivo JSON (Javascript Object Notation)

from urllib.request import Request, urlopen

url = Request("http://globalmentoring.com.mx/api/personas.json")
url.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15')

request = urlopen(url)

print(f"Respuesta del servidor:\n{request}")

body = request.read()
print(f"Cuerpo del documento:\n{body}")
