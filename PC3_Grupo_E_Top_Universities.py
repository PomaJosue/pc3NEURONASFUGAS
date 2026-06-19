# PC3 - Grupo E: Top Universities / QS World University Rankings
# Tema: Expresiones Regulares, Programas en Red y Web Scraping
# Librerías usadas: re, requests, BeautifulSoup, pandas y matplotlib

import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# PARTE I. PROGRAMAS EN RED
# ============================================================

import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL asignada al grupo E
url = "https://www.topuniversities.com/world-university-rankings"

# Headers para simular una petición desde navegador
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Realizamos la conexión HTTP
respuesta = requests.get(url, headers=headers)

# Mostramos el código de estado
print("URL consultada:", url)
print("Status code:", respuesta.status_code)

# Explicamos el significado del status_code
if respuesta.status_code == 200:
    print("Significado: 200 indica que la petición HTTP fue exitosa.")
else:
    print("Significado: hubo un problema con la petición HTTP.")

# Mostramos el tipo de contenido recibido
content_type = respuesta.headers.get("Content-Type")
print("Content-Type recibido:", content_type)

# ============================================================
# PARTE II. RECUPERACIÓN DE DATOS
# Primer punto: obtener al menos 15 registros desde la página web
# ============================================================

# Convertimos el contenido HTML en un objeto BeautifulSoup
soup = BeautifulSoup(respuesta.text, "html.parser")

# Obtenemos textos visibles de la página
textos = soup.get_text("\n", strip=True).split("\n")

# Limpiamos los textos vacíos o demasiado cortos
registros = []

for texto in textos:
    texto = texto.strip()
    
    if len(texto) > 5:
        registros.append(texto)

# Tomamos los primeros 15 registros encontrados en la página
registros_15 = registros[:15]

print("Cantidad de registros obtenidos:", len(registros_15))

for i, registro in enumerate(registros_15, start=1):
    print(i, "-", registro)