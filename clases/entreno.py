class Entreno:
    def __init__(self, fecha=None, tipo_de_entreno=None):
        self.fecha = fecha
        self.tipo_de_entreno = tipo_de_entreno
        self.ejercicios = []

    def getInfo(self):
        print(self.fecha)
        print(self.tipo_de_entreno)
        for ejercicio in self.ejercicios:
            ejercicio.getInfo()

    def getFecha(self):
        return self.fecha

    def getTipoDeEntreno(self):
        return self.tipo_de_entreno

    def getEjercicios(self):
        return self.ejercicios

    def setFecha(self, fecha):
        self.fecha = fecha
