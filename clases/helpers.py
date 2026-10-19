from clases.ejercicio import Ejercicio
from clases.entreno import Entreno
from clases.serie import Serie


def entreno_maker(sesion, numeros_emojis):
    entrenamiento = Entreno()

    for linea in sesion:
        linea_dividida = linea.split()

        # Añadir lectura de fechas
        # Me acabo de dar cuenta que la fecha está en el nombre
        # del archivo, es mejor cogerla de ahí, para asegurar y evitar errores.
        # PENDIENTE
        if "📅" in linea_dividida:
            linea_dividida.pop(0)
            linea_dividida.pop(0)
            fecha = " ".join(linea_dividida)
            entrenamiento.fecha = fecha

        # Añadir lectura de tipo de entreno
        # Aquí se mira si una string es
        if "💪" in linea_dividida or "🦵" in linea_dividida:
            if linea_dividida[4] == "BRAZOS":
                entrenamiento.tipo_de_entreno = linea_dividida[4]
            else:
                entrenamiento.tipo_de_entreno = (
                    linea_dividida[4] + " " + linea_dividida[5]
                )

        for num in numeros_emojis:
            if num in linea_dividida:
                linea_dividida.pop(0)
                nombre_ejercicio = " ".join(linea_dividida)
                ejercicio_actual = Ejercicio(nombre_ejercicio)
                entrenamiento.ejercicios.append(ejercicio_actual)
                break

        serie = Serie()

        if any(s in linea_dividida for s in ("S1:", "S2:", "S3:", "S4:")):
            if "s" in linea_dividida:
                if "/" in linea_dividida:
                    # Aquí segundos con kg
                    posicion = linea_dividida.index("/")
                    serie.peso = linea_dividida[posicion - 1]
                    serie.seg = linea_dividida[posicion + 1]
                else:
                    # Aquí solo segundos
                    posicion = linea_dividida("s")
                    serie.seg = linea_dividida[posicion - 1]

                serie.numero = linea_dividida[0]
                ejercicio_actual.series.append(serie)
            else:
                posicion = linea_dividida.index("/")
                serie.peso = linea_dividida[posicion - 1]
                serie.repes = linea_dividida[posicion + 1]
                serie.numero = linea_dividida[0]
                ejercicio_actual.series.append(serie)

        if "izq:" in linea_dividida or "der:" in linea_dividida:
            try:
                posicion = linea_dividida.index("/")
                serie.peso = linea_dividida[posicion - 1]
                serie.repes = linea_dividida[posicion + 1]
                serie.numero = linea_dividida[0]
                ejercicio_actual.series.append(serie)

            except ValueError:
                # Si hay error, el programa no peta y muestra la línea.
                print(linea_dividida)

    return entrenamiento
