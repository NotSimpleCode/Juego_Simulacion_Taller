import Montecarlo as MC
import Markov as MK

class PowerUpMarkovClass():
    def __init__(self):
        
        probsMunicion = {
            39 : 1, #Municion - obtener municion
            50 : 2, #Municion - obtener vida
            10 : 3, #Municion - obtener doble_poder
            1 : 4  #Municion - obtener puntos_extra
        }
        municion = MC.run(probsMunicion, 100000)

        probsVida = {
            60 : 1, #Vida - obtener municion
            30 : 2, #Vida - obtener vida
            9 : 3, #Vida - obtener doble_poder
            1 : 4  #Vida - obtener puntos_extra
        }
        vida = MC.run(probsVida, 100000)

        probsdoble_poder = {
            44 : 1, #doble_poder - obtener municion
            5 : 2, #doble_poder - obtener vida
            1 : 3, #doble_poder - obtener doble_poder
            50 : 4  #doble_poder - obtener puntos_extra
        }
        doble_poder = MC.run(probsdoble_poder, 100000)

        probspuntos_extra = {
            80 : 1, #puntos_extra - obtener municion
            15 : 2, #puntos_extra - obtener vida
            4 : 3,  #puntos_extra - obtener doble_poder
            1 : 4   #puntos_extra - obtener puntos_extra
        }
        puntos_extra = MC.run(probspuntos_extra, 100000)

        estados_nombres = {
            1 : "bullet_refill",
            2 : "health",
            3 : "double_refill",
            4 : "extra_points"
        }

        montecarlosProbs = {
            1 : municion,
            2 : vida,
            3 : doble_poder,
            4 : puntos_extra
        }

        self.markov = MK.run(estados_nombres,montecarlosProbs)

    def obtenerSiguientePoder(self):
        self.markov.obtenerSiguienteEstado()
        return self.markov.obtenerNombreEstado()

"""
Ejemplo de uso de la clase, cada vez que se llame la funcion obtenerSiguientePoder() se calcula el siguiente poder 
"""
#powerUps = PowerUpMarkovClass()
#for i in range(1000):
#    print(powerUps.obtenerSiguientePoder())
