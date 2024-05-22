import Montecarlo as MC


class DisparoMontecarloClass():
    def __init__(self):
        self.valores_probabilidad_disparo = {
            60 : 10,  #60 % de probabilidad de hacer 10 de daño - impacto al cuerpo
            20 : 20,  #20 % de probabilidad de hacer 20 de daño - impacto a piernas
            15 : 30,  #15 % de probabilidad de hacer 30 de daño - impactos a brazos
            5 : 60    #5 % de probabilidad de hacer 60 de daño - impacto a cabeza
        }
        self.mimonte = MC.run(self.valores_probabilidad_disparo, 100000)
    

    def obtenerDisparo(self):
        if self.mimonte!=None: 
            return self.mimonte.calcularResultado() 
        else: return 0

    def cambiar_probabilidades(self,probs):
        self.valores_probabilidad_disparo = probs
        self.mimonte = self.mimonte.cambiarProbabilidades(self.valores_probabilidad_disparo)