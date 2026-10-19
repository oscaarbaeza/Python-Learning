import os
import sys
from datetime import datetime

import matplotlib.pyplot as plt

from clases.entreno import Entreno
from clases.helpers import entreno_maker

# Guardar aquí todos los entrenos.
lista_entrenos = []

# El número máximo de ejercicios en mi rutina de gym son 10. Si esto sube, tendría
# que venir al programa y añadir nuevos números (o quitarlos).
numeros_emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

ruta_carpeta = "sesiones"

elementos = os.listdir(ruta_carpeta)

entreno = Entreno()

for nombre in os.listdir(ruta_carpeta):
    ruta_archivo = ruta_carpeta + "/" + nombre
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        # nombre_separado = nombre.split("-")
        # entreno.setFecha(nombre_separado[-2])
        entreno = entreno_maker(lineas, numeros_emojis)
        lista_entrenos.append(entreno)
    else:
        print("Error de lectura.")
        sys.exit(1)

# Mostrar toda la información de los entrenamientos, texto.
# for training in lista_entrenos:
#     training.getInfo()

diccionario_entrenos = {}
for training in lista_entrenos:
    for ejercicio in training.getEjercicios():
        # Si el ejercicio no existe como key en el diccionario, se añade.
        if not any(s == ejercicio.getNombre() for s in diccionario_entrenos):
            diccionario_entrenos[ejercicio.getNombre()] = []

        # Aquí me haría falta saber cómo interpretar lo de los segundos
        total_volumen_ejercicio = 0.0
        for serie in ejercicio.getSeries():
            # serie.getInfo()
            if serie.getSegundos() != 0:
                total_volumen_ejercicio += serie.getSegundos()
            else:
                total_volumen_ejercicio += serie.volumen_serie()

        diccionario_entrenos[ejercicio.getNombre()] += [
            (total_volumen_ejercicio, training.getFecha())
        ]

print(diccionario_entrenos)
# Dibujar una gráfica por ejercicio, mostrando progreso temporal.

for ejercicio, series in diccionario_entrenos.items():
    # Voy a ordenar por fecha los entrenos.
    series_ordenadas = sorted(series, key=lambda x: datetime.strptime(x[1], "%d %b %Y"))
    eje_y, eje_x = zip(*series_ordenadas)
    plt.title(ejercicio)
    plt.bar(eje_x, eje_y)
    plt.ylabel("kg peso")
    plt.xlabel("fecha")
    plt.xticks(rotation=45, fontsize=10, ha="right")
    plt.show()
