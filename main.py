"""
Imagina que esta API es una biblioteca de peliculas:
La funcion load_movies() es como un bibliotecario que carga el cataogo de
libros (peliculas) cuando se abre la biblioteca.
La funcion get_movies() muestra todo el catalogo cuando alguien lo pide.
La funcion get_movie() es como si alguien preguntara por uin libro especifico
por su codigo de identificacion.
La funcion chatbot (query) es un asistente que busca libros segun palabras clave
y sinonimo.
La funcion get_movie_by_category (category) ayuda a encontrar peliculas segun su
genero (accion, comedia, etc).
"""

# Importamos las herramientas necesarias para construir nuestra API
from fastapi import FastAPI, HTTPException  # FastAPI nos ayuda a crear la API, HTTPException maneja errores.
from fastapi.responses import HTMLResponse, JSONResponse  # HTMLResponse para paginas web, JSONResponse para respuestas en formato JSON
import pandas as pd  # Pandas es una herramienta para manejar datos en tablas.
import nltk  # NLTK es una herramienta para procesar texto y analizar palabras.
from nltk.tokenize import word_tokenize  # Se usa para dividir un texto en palabras individuales.
from nltk.corpus import wordnet  # Nos ayuda a encontrar sinónimos de palabras.

# Indicamos la ruta donde NLTK buscará los datos descargados en nuestro computador.
nltk.data.path.append("/opt/homebrew/lib/python3.9/site-packages/nltk_data")

# Descargar las herramientas necesarias de NLTK para el analisis de palabras.abs

nltk.download("punkt")  # Herramienta para dividir frases en palabras.
nltk.download("wordnet")  # Herramienta para encontrar sinónimos de palabras en ingles.

# Funcion para cargar ls peliculas desde un archivo CSV.


def load_movies():
    # Leemos el archivo que contiene la informacion de las peliculas y seleccionamos las columnas importantes
    df = pd.read_csv("Dataset/netflix_titles.csv")[['show_id', 'title', 'release_year', 'listed_in', 'rating', 'description']]

    # Renombramos las columnas para que sean mas faciles de entender
    df.columns = ['id', 'title', 'year', 'category', 'rating', 'description']

    # Llenamos los espacios vacios con texto vacio y convertimos los datos en una lista de diccionarios
    return df.fillna('').to_dict(orient='records')
