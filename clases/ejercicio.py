class Ejercicio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.series = []

    def getInfo(self):
        print(self.nombre)
        for serie in self.series:
            serie.getInfo()

    def getNombre(self):
        return self.nombre

    def getSeries(self):
        return self.series
