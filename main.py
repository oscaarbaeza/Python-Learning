import os
import sys

import matplotlib.pyplot as plt


def volumen_serie(serie):

    if "s" in serie:
        return float(serie[1])

    posicion = serie.index("/")
    peso = serie[posicion - 1]
    reps = serie[posicion + 1]

    return float(peso) * float(reps)


ruta_archivo = "sesiones/12 oct upper a_61013_202507.txt"

if os.path.exists(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
else:
    print("Error de lectura.")
    sys.exit(1)

# El número máximo de ejercicios en mi rutina de gym son 10. Si esto sube, tendría
# que venir al programa y añadir nuevos números (o quitarlos).
numeros_emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

volumen_ejercicios = {}

ejercicio_actual = None

for linea in lineas:
    linea_dividida = linea.split()

    for num in numeros_emojis:
        if num in linea_dividida:
            ejercicio_actual = " ".join(linea_dividida).title()
            volumen_ejercicios[ejercicio_actual] = {
                "total": 0,
                "izq": 0,
                "der": 0,
                "segundos": {"s": 0, "repes": 0},
            }
            break
    # Hay que entender primero esta línea, antes de pasar el proyecto
    if any(s in linea_dividida for s in ("S1:", "S2:", "S3:", "S4:")):
        if "s" in linea_dividida:
            volumen_ejercicios[ejercicio_actual]["segundos"]["s"] = volumen_ejercicios[
                ejercicio_actual
            ]["segundos"]["s"] + volumen_serie(linea_dividida)
            volumen_ejercicios[ejercicio_actual]["segundos"]["repes"] += 1
        else:
            volumen_ejercicios[ejercicio_actual]["total"] = volumen_ejercicios[
                ejercicio_actual
            ]["total"] + volumen_serie(linea_dividida)

    if "izq:" in linea_dividida:
        volumen_ejercicios[ejercicio_actual]["izq"] = volumen_ejercicios[
            ejercicio_actual
        ]["izq"] + volumen_serie(linea_dividida)
    elif "der:" in linea_dividida:
        volumen_ejercicios[ejercicio_actual]["der"] = volumen_ejercicios[
            ejercicio_actual
        ]["der"] + volumen_serie(linea_dividida)

# Ahora mismo hay como un popurri de información que no interesa
# Podría hacer una ultima funcion que lo limpiara todo si el campo es 0

pesos = []
for ejercicio in volumen_ejercicios.values():
    pesos.append(ejercicio["total"])

plt.bar(volumen_ejercicios.keys(), pesos)
plt.ylabel("kg peso")
plt.xlabel("ejercicios")
plt.xticks(rotation=45, fontsize=10, ha="right")
plt.show()
