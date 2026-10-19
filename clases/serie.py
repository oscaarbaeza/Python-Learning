class Serie:
    def __init__(self, numero="", peso=0, repes=0, seg=0, izq=0, der=0):
        self.numero = numero
        self.peso = peso
        self.repes = repes
        self.seg = seg
        self.izq = izq
        self.der = der

    def volumen_serie(self):
        if self.izq != 0:
            return float(self.repes) * float(self.izq)
        if self.der != 0:
            return float(self.repes) * float(self.der)

        return float(self.peso) * float(self.repes)

    def getInfo(self):
        print(
            self.numero
            + " "
            + str(self.peso)
            + "kg-"
            + str(self.repes)
            + "rps-"
            + str(self.seg)
            + "s-"
            + str(self.izq)
            + "kgIzq-"
            + str(self.der)
            + "kgDer"
        )

    def getSegundos(self):
        return self.seg

    def getPeso(self):
        return self.peso
