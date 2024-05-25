import riManage

class CaminataHVD():
    def __init__(self):
        self.datos = []
        self.resultado = None
        self.manejoRi = riManage.riManage()
        self.manejoRi.generarNumerosHastaPasarPruebas(100000)

    def obtener_direccion(self, umbral=0.125):
        indato = self.manejoRi.obtenerRandom(100000)
        if indato <= umbral:
            self.resultado = (-1, 0)  # Izquierda
        elif indato > umbral and indato <= umbral * 2:
            self.resultado = (1, 0)  # Derecha
        elif indato > umbral * 2 and indato <= umbral * 3:
            self.resultado = (0, 1)  # Arriba
        elif indato > umbral * 3 and indato <= umbral * 4:
            self.resultado = (0, -1)  # Abajo
        elif indato > umbral * 4 and indato <= umbral * 5:
            self.resultado = (-1, 1)  # izquierda arriba
        elif indato > umbral * 5 and indato <= umbral * 6:
            self.resultado = (1, 1)  # derecha arriba
        elif indato > umbral * 6 and indato <= umbral * 7:
            self.resultado = (-1, -1)  # izquierda abajo
        else:
            self.resultado = (1, -1)  # derecha abajo
        return self.resultado

