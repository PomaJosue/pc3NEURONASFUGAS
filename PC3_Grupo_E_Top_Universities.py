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


# ============================================================
# PC3 - GRUPO E: TOP UNIVERSITIES
# Parte I y primer punto de Parte II
# ============================================================

import requests
from bs4 import BeautifulSoup
import pandas as pd


# ============================================================
# PARTE I. PROGRAMAS EN RED
# ============================================================

# URL asignada al grupo E
url = "https://www.topuniversities.com/world-university-rankings"

# Se agrega User-Agent para simular una consulta desde navegador
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Realizamos la conexión mediante requests
respuesta = requests.get(url, headers=headers)

# Mostramos la URL consultada
print("URL consultada:", url)

# Mostramos el status_code
print("Status code:", respuesta.status_code)

# Explicamos el significado del status_code
if respuesta.status_code == 200:
    print("Significado: 200 indica que la petición HTTP fue exitosa.")
else:
    print("Significado: el código recibido indica que la petición no fue exitosa.")

# Mostramos el Content-Type recibido
content_type = respuesta.headers.get("Content-Type")
print("Content-Type recibido:", content_type)


# ============================================================
# PARTE II. RECUPERACIÓN DE DATOS
# Primer punto: obtener al menos 15 registros desde la página web
# ============================================================

# Procesamos el contenido HTML recibido
soup = BeautifulSoup(respuesta.text, "html.parser")

# Extraemos todos los textos visibles del HTML
textos = soup.get_text("\n", strip=True).split("\n")

# Limpiamos los textos obtenidos
registros = []

for texto in textos:
    texto = texto.strip()

    # Filtramos textos vacíos o demasiado cortos
    if len(texto) > 5:
        registros.append(texto)

# Obtenemos al menos 15 registros
registros_15 = registros[:15]

# Mostramos los registros encontrados
print("\nCantidad de registros obtenidos:", len(registros_15))
print("\nRegistros obtenidos desde la página:")

for i, registro in enumerate(registros_15, start=1):
    print(i, "-", registro)


# Opcional: crear un DataFrame para visualizar mejor los registros
df_registros = pd.DataFrame(registros_15, columns=["Registro"])

print("\nDataFrame con los primeros 15 registros:")
print(df_registros)

# ============================================================
# PARTE II. RECUPERACIÓN DE DATOS
# Segundo punto: extraer tres atributos relevantes para el análisis
# Tercer punto: utilizar expresión regular
# ============================================================

import re

datos = []

for i, registro in enumerate(registros_15, start=1):

    # Atributo 1: número de registro
    numero_registro = i

    # Atributo 2: texto del registro obtenido desde la página
    texto_registro = registro

    # Atributo 3: cantidad de caracteres del registro
    cantidad_caracteres = len(registro)

    # Expresión regular:
    # Extrae números que aparezcan dentro del texto, por ejemplo años, cantidades o posiciones.
    numeros_extraidos = re.findall(r"\d+", registro)

    datos.append({
        "Numero": numero_registro,
        "Registro": texto_registro,
        "Cantidad_caracteres": cantidad_caracteres,
        "Numeros_extraidos_regex": numeros_extraidos
    })

print("Datos con tres atributos y uso de expresión regular:")

for dato in datos:
    print(dato)