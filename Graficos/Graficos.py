import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Crea una variable para almacenar el archivo *.xlsx
tabla = "../Rating/Tabla FIDE - Clasificación Mundial de Ajedrez.xlsx"

#DataFrame del archivo
df = pd.read_excel(tabla)


#Creamos un diccionario con los datos que nos interesan para graficar
valores = df[["Name", "Fed"]]
repeticiones = {}
for n in valores["Fed"]:
  if n in repeticiones:
    repeticiones[n] += 1
  else:
    repeticiones[n] = 1


#Agregando a una lista los nombres
paises = []
for i in repeticiones.keys():
  paises.append(i)

#Agregando a una lista los valores repetidos (cantidad de jugadores del mismo pais)
valores = []
for i in repeticiones.values():
  valores.append(i)

#Convirtiendo las listas en Arrays
y = np.array(valores)
x = np.array(paises)

	#########################################################################
	##### HACIENDO UN GRAFICO DE BARRAS PARA REPRESENTAR LOS RESULTADOS #####
	#########################################################################

#Aumentamos el tamaño del grafico
plt.figure(figsize=(15,8))

#Colocamos un título para el gráfico
plt.title("Participación de Paises en el Top 100")

#El nombre para el eje de las "x" e "y", respectivamente.
plt.xlabel("Paises")
plt.ylabel("Cantidad de Jugadores")

#Creando el gráfico, cambiando tanto el color como el ancho de las barras.
plt.bar(x, y, color="blue", width=0.4)

#Mostrando el gráfico
plt.show()


	#########################################################################
	##### HACIENDO UN GRAFICO DE TORTA PARA REPRESENTAR LOS RESULTADOS ######
	#########################################################################

edades = df[["Year"]]

#Creando variables para almacenar la cantidad de personas según la edad
hasta20 = 0
de21a30 = 0
de31a40 = 0
de41a50 = 0
mas50 = 0

for i in edades["Year"]:
  if i <= 20:
   hasta20 += 1
  elif i > 20 and i < 31:
    de21a30 += 1
  elif i > 30 and i < 41:
    de31a40 += 1
  elif i > 40 and i < 51:
    de41a50 += 1
  else:
    mas50 += 1

###SOLO TESTEO###
#print("Hasta 20:", hasta20)
#print("De 21 a 30:", de21a30)
#print("De 31 a 40:", de31a40)
#print("De 41 a 50: ", de41a50)
#print("Mas 50: ", mas50)

#Hago una array con la cantidad de personas según la edad.
datos_completo = [hasta20, de21a30, de31a40, de41a50, mas50]

condicion = [f"Hasta de 20 Años = {hasta20}",
			f"De 21 a 30 Años = {de21a30}",
			f"De 31 a 40 Años = {de31a40}",
			f"De 41 a 50 Años = {de41a50}",
			f"Más de 50 Años = {mas50}"]

desfase = (0, 0, 0.1, 0, 0)
plt.figure(figsize=(15,10)) 
plt.pie(datos_completo, labels = condicion, autopct="%0.1f %%", explode=desfase)

plt.title("Participación por rangos de edades (Años)")
plt.show()
