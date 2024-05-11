import Montecarlo as MC
import Markov as MK

class PowerUpMarkovClass():
    def __init__(self):
        
        probsMunicion = {
            10 : 1, #Municion - obtener municion
            40 : 2, #Municion - obtener vida
            30 : 3, #Municion - obtener velocidad
            20 : 4  #Municion - obtener escudo
        }
        municion = MC.run(probsMunicion, 100000)

        probsVida = {
            40 : 1, #Vida - obtener municion
            10 : 2, #Vida - obtener vida
            20 : 3, #Vida - obtener velocidad
            30 : 4  #Vida - obtener escudo
        }
        vida = MC.run(probsVida, 100000)

        probsVelocidad = {
            15 : 1, #Velocidad - obtener municion
            15 : 2, #Velocidad - obtener vida
            10 : 3, #Velocidad - obtener velocidad
            60 : 4  #Velocidad - obtener escudo
        }
        velocidad = MC.run(probsVelocidad, 100000)

        probsEscudo = {
            80 : 1, #Escudo - obtener municion
            10 : 2, #Escudo - obtener vida
            5 : 3,  #Escudo - obtener velocidad
            5 : 4   #Escudo - obtener escudo
        }
        escudo = MC.run(probsEscudo, 100000)

        estados_nombres = {
            1 : "municion",
            2 : "vida",
            3 : "velocidad",
            4 : "escudo"
        }

        montecarlosProbs = {
            1 : municion,
            2 : vida,
            3 : velocidad,
            4 : escudo
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
