class Serie:
    def __init__(self, peso, repes, seg, izq, der):
        self.peso = peso
        self.repes = repes
        self.seg = seg
        self.izq = izq
        self.der = der

    def volumen_serie(serie):

        if "s" in serie:
            return float(serie[1])

        posicion = serie.index("/")
        peso = serie[posicion - 1]
        reps = serie[posicion + 1]

        return float(peso) * float(reps)
