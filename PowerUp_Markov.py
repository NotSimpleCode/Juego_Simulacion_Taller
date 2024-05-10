import Montecarlo as MC
import Markov as MK

class PowerUpMarkovClass():
    def __init__(self):
        
        valores = {
        60 : 1,
        40 : 2
        }
        mimonte = MC.run(valores, 100000)

        valores2 = {
            20 : 2,
            80 : 1
        }
        mimonte2 = MC.run(valores2, 100000)

        estados_nombres = {
            1 : "Frio",
            2 : "Calor"
        }

        montecarlosProbs = {
            1 : mimonte,
            2 : mimonte2
        }

        self.markov = MK.run(estados_nombres,montecarlosProbs)

    def obtenerSiguientePoder(self):
        self.markov.obtenerSiguienteEstado()
        return self.markov.obtenerNombreEstado()

"""
Ejemplo de uso de la clase, cada vez que se llame la funcion obtenerSiguientePoder() se calcula el siguiente poder 
"""
powerUps = PowerUpMarkovClass()
for i in range(100000):
    print(powerUps.obtenerSiguientePoder())
