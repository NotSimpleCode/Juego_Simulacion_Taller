import Montecarlo as MC


class DisparoMontecarloClass():
    def __init__(self):
        self.valores_probabilidad_disparo = {
            60 : 1,  #60 % de probabilidad de hacer 1 de daño
            20 : 2,  #20 % de probabilidad de hacer 2 de daño
            15 : 3,  #15 % de probabilidad de hacer 3 de daño
            5 : 6    #5 % de probabilidad de hacer 6 de daño
        }
        self.mimonte = MC.run(self.valores_probabilidad_disparo, 100000)
    

    def obtenerDisparo(self):
        if self.mimonte!=None: 
            return self.mimonte.calcularResultado() 
        else: return 0

    def cambiar_probabilidades(self,probs):
        self.valores_probabilidad_disparo = probs
        self.mimonte = self.mimonte.cambiarProbabilidades(self.valores_probabilidad_disparo)