texto = """
1️⃣
PESO MUERTO RUMANO (STRAPS)
3×6-10 · RIR 1-2 · 3 min
💡 Cadera atrás, barra pegada, espalda recta.
Grábate de lado
📊 Ref: 35 → 10 a RIR 3 · lumbar 5-6
🎯 Si la lumbar fue dolor: 35 y técnica · si fue
trabajo: 40
S1: 40 / 10 / 2 o 3
S2: 40 / 7 / podia mas
S3: 40 / 7 / podia mas
Lumbar (0-10, ¿dolor o trabajo?):
Notas: vale, en la segunda he parao por el
agarre, tengo q coger los straps para la proxima.
Tampoco he sentido mucho los isquios, hay q
mejorar en la concentracion. Lo de la bosagra lo
hice y los sentia q flipas como se extiraba, hay q
practicar mas eso
"""

lineas = texto.splitlines()
nombre_ejercicio = lineas[2]

serie_1 = lineas[9]
serie_2 = lineas[10]
serie_3 = lineas[11]

# Prueba de que se pueden coger letras 
# de los string y juntarlas después
# string = "HOALLALALA  O"
# letra_h = string[0] + string[1] # HO

serie_1_kilos = int(serie_1[4] + serie_1[5]) * int(serie_1[9] + serie_1[10])
serie_2_kilos = int(serie_2[4] + serie_2[5]) * int(serie_2[9])
serie_3_kilos = int(serie_3[4] + serie_3[5]) * int(serie_3[9])

total_kg = str(serie_1_kilos + serie_2_kilos + serie_3_kilos)

print(nombre_ejercicio.title() + ": " + total_kg + " kg")