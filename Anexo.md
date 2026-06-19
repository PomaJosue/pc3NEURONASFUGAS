````md
# ANEXO: USO RESPONSABLE DE INTELIGENCIA ARTIFICIAL

## 1. Prompts utilizados

Durante el desarrollo de la práctica, la Inteligencia Artificial fue utilizada como una herramienta de apoyo para orientar la estructura del trabajo, revisar la lógica del código y comprender mejor el uso de las librerías empleadas en clase. Los prompts fueron formulados para recibir guía y explicación, manteniendo la revisión y adaptación final a cargo del grupo.

### Prompt 1

> Ayúdame a organizar la Parte I de la práctica usando únicamente la URL asignada de Top Universities. Necesito realizar una conexión con `requests`, mostrar el `status_code`, explicar su significado e indicar el `Content-Type` recibido.

### Prompt 2

> Explícame cómo obtener al menos 15 registros desde la página web asignada utilizando `requests` y `BeautifulSoup`, de una forma sencilla y similar a lo trabajado en clase.

### Prompt 3

> Ayúdame a identificar tres atributos relevantes que puedan extraerse de los registros recuperados desde la página web para iniciar el análisis de datos.

### Prompt 4

> Explícame cómo aplicar una expresión regular con `re.findall` para extraer patrones numéricos dentro de los textos obtenidos desde la página web.

### Prompt 5

> Ayúdame a crear un `DataFrame` con `pandas` a partir de los registros recuperados y de los atributos definidos para el análisis.

### Prompt 6

> Indícame cómo limpiar o transformar los datos del `DataFrame`, eliminando espacios, uniformizando el texto y creando columnas adicionales cuando sea necesario.

### Prompt 7

> Ayúdame a obtener tres estadísticas descriptivas relevantes a partir del `DataFrame` generado y a redactar una explicación breve sobre qué aportan esos resultados.

### Prompt 8

> Ayúdame a generar un gráfico de barras con `matplotlib` para visualizar los datos obtenidos e interpretar brevemente el resultado.

---

## 2. Respuesta proporcionada por la IA

La IA brindó una orientación general para desarrollar la práctica de forma ordenada, respetando las partes solicitadas en el enunciado.

En primer lugar, sugirió utilizar `requests.get()` para realizar la conexión HTTP a la URL asignada, mostrar el `status_code`, explicar que el código `200` representa una petición exitosa y obtener el `Content-Type` desde los encabezados de la respuesta.

Luego, recomendó procesar el contenido HTML con `BeautifulSoup`, extraer textos visibles de la página y seleccionar al menos 15 registros para cumplir con la recuperación inicial de datos.

Para la extracción de atributos, la IA propuso trabajar con variables simples y verificables:

- Número de registro.
- Texto del registro.
- Cantidad de caracteres.

Asimismo, explicó cómo utilizar la expresión regular:

```python
re.findall(r"\d+", registro)
````

con la finalidad de identificar patrones numéricos dentro de los textos recuperados.

En la etapa de procesamiento, sugirió crear un `DataFrame` con `pandas`, limpiar los textos mediante `.str.strip()`, crear nuevas columnas y obtener estadísticas descriptivas como:

* Total de registros.
* Promedio de caracteres.
* Registro con mayor cantidad de caracteres.
* Cantidad de registros que contienen números.

Finalmente, propuso elaborar un gráfico de barras con `matplotlib`, utilizando el número de registro en el eje X y la cantidad de caracteres en el eje Y, con una breve interpretación sobre la extensión de los registros obtenidos.

El grupo revisó la propuesta, adaptó el código al enlace asignado, organizó los comentarios y distribuyó el desarrollo conforme a la participación de cada integrante.

---

## 3. Tabla de participación y aprendizaje

| Integrante   | Prompt utilizado                                                                                                                                                                                                                                                                                                      | Qué modificó del código generado                                                                                                                                                                         | Qué aprendió gracias a la IA                                                                                                                                            |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Integrante 1 | Ayúdame a organizar la Parte I de la práctica usando únicamente la URL asignada de Top Universities. Necesito realizar una conexión con `requests`, mostrar el `status_code`, explicar su significado e indicar el `Content-Type` recibido. Además, orienta cómo recuperar al menos 15 registros desde la página web. | Desarrolló la conexión con `requests`, verificó el `status_code`, mostró la URL consultada y el `Content-Type`. También organizó la primera recuperación de registros desde el HTML con `BeautifulSoup`. | Aprendió a validar una respuesta HTTP, interpretar el código `200`, revisar los encabezados de una respuesta web y recuperar registros iniciales desde una página HTML. |
| Integrante 2 | Ayúdame a extraer tres atributos relevantes de los registros obtenidos y a utilizar una expresión regular para identificar patrones dentro del texto. También orienta cómo crear un `DataFrame` con `pandas`.                                                                                                         | Definió los atributos de análisis: número de registro, texto del registro y cantidad de caracteres. Aplicó `re.findall()` para extraer números y creó el `DataFrame` inicial con `pandas`.               | Aprendió a estructurar datos recuperados desde una página web, aplicar expresiones regulares y organizar la información en un `DataFrame`.                              |
| Integrante 3 | Indícame cómo limpiar o transformar los datos del `DataFrame`, obtener tres estadísticas descriptivas relevantes y redactar una explicación breve sobre los resultados.                                                                                                                                               | Limpió los textos con `.str.strip()`, creó columnas adicionales, eliminó duplicados y calculó estadísticas como total de registros, promedio de caracteres y registro con mayor cantidad de caracteres.  | Aprendió a transformar datos con `pandas`, crear variables derivadas y explicar la utilidad de las estadísticas descriptivas en el análisis.                            |
| Integrante 4 | Ayúdame a generar un gráfico adecuado con `matplotlib` para visualizar los datos obtenidos e interpretar brevemente el resultado.                                                                                                                                                                                     | Generó el gráfico de barras, agregó título, etiquetas de ejes y redactó la interpretación final del gráfico.                                                                                             | Aprendió a visualizar datos con `matplotlib` y a interpretar un gráfico en función de los registros analizados.                                                         |

---

## 4. Declaración de uso responsable

La Inteligencia Artificial fue utilizada como una herramienta de apoyo para orientar el desarrollo de la práctica, resolver dudas sobre el uso de librerías y mejorar la organización del código.

El grupo revisó, adaptó y validó la propuesta final, asegurando que se utilice la fuente asignada y que cada integrante comprenda la parte desarrollada.

Asimismo, la IA no reemplazó la participación de los integrantes, sino que sirvió como apoyo para reforzar la comprensión de los temas trabajados en clase: `requests`, `BeautifulSoup`, expresiones regulares, `pandas` y visualización de datos.

```
```
