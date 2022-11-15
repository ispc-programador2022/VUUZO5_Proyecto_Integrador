
from bs4 import BeautifulSoup
import requests
import pandas as pd

# El código abre el archivo "home.html", el cuál contiene una tabla con los datos de 102 jugadores de ajedrez mundial.
# Datos que se solicitan: Calificación del jugador, Nombre completo, Nacionalidad, Puntos Elo y Año de Nacimiento.

with open ('home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    clasificacion_tags = soup.find_all('tr')

    for clasificacion in clasificacion_tags:
        print(clasificacion.text)


        