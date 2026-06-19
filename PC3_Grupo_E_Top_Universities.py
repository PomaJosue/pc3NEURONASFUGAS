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


    # ============================================================
# PARTE II Y PARTE III LIZ
# Extracción de atributos, uso de regex y creación de DataFrame
# ============================================================

import re
import pandas as pd

datos = []

for i, registro in enumerate(registros_15, start=1):

    numero_registro = i
    texto_registro = registro
    cantidad_caracteres = len(registro)

    # Regex para extraer números dentro del texto
    numeros_extraidos = re.findall(r"\d+", registro)

    datos.append({
        "Numero": numero_registro,
        "Registro": texto_registro,
        "Cantidad_caracteres": cantidad_caracteres,
        "Numeros_extraidos_regex": numeros_extraidos
    })

# Crear DataFrame con pandas
df = pd.DataFrame(datos)

print("DataFrame creado con pandas:")
print(df)

# ============================================================
# PARTE III. PROCESAMIENTO Y ANÁLISIS LIZ 1
# Limpieza o transformación de datos
# ============================================================

# Limpiamos espacios al inicio y final del texto
df["Registro_limpio"] = df["Registro"].str.strip()

# Convertimos el texto a formato uniforme
df["Registro_limpio"] = df["Registro_limpio"].str.replace("\n", " ", regex=False)

# Creamos una nueva columna con la cantidad de números encontrados por regex
df["Cantidad_numeros_regex"] = df["Numeros_extraidos_regex"].apply(len)

# Creamos una columna para identificar si el registro contiene números
df["Tiene_numeros"] = df["Cantidad_numeros_regex"] > 0

# Eliminamos posibles registros duplicados
df = df.drop_duplicates(subset=["Registro_limpio"])

print("DataFrame limpio y transformado:")
print(df)


# ============================================================
# Estadísticas descriptivas relevantes LIZ 2
# ============================================================

# 1. Cantidad total de registros analizados
total_registros = len(df)

# 2. Promedio de caracteres por registro
promedio_caracteres = df["Cantidad_caracteres"].mean()

# 3. Registro con mayor cantidad de caracteres
max_caracteres = df["Cantidad_caracteres"].max()

# Estadística adicional: cantidad de registros que contienen números
registros_con_numeros = df["Tiene_numeros"].sum()

print("Estadísticas descriptivas:")
print("1. Total de registros analizados:", total_registros)
print("2. Promedio de caracteres por registro:", round(promedio_caracteres, 2))
print("3. Mayor cantidad de caracteres en un registro:", max_caracteres)
print("4. Registros que contienen números:", registros_con_numeros)

# ============================================================
# PARTE IV. VISUALIZACIÓN
# Generar un gráfico adecuado e interpretar el resultado
# ============================================================

import matplotlib.pyplot as plt

# Gráfico de barras:
# Muestra la cantidad de caracteres que tiene cada registro recuperado

plt.figure(figsize=(10, 5))

plt.bar(df["Numero"], df["Cantidad_caracteres"])

plt.title("Cantidad de caracteres por registro obtenido")
plt.xlabel("Número de registro")
plt.ylabel("Cantidad de caracteres")

plt.xticks(df["Numero"])
plt.tight_layout()

plt.show()

# Interpretación breve del gráfico
print("Interpretación:")
print("El gráfico de barras permite comparar la extensión de cada registro obtenido desde la página web.")
print("Los registros con mayor cantidad de caracteres contienen más información textual y pueden aportar más datos para el análisis.")