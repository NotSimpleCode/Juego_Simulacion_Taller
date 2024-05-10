import Montecarlo as MC


class DisparoMontecarloClass():
    def __init__(self):
        self.valores_probabilidad_disparo = {
            60 : 1,
            20 : 2,
            15 : 3,
            5 : 6
        }
        self.mimonte = MC.run(self.valores_probabilidad_disparo, 100000)
    

    def obtenerDisparo(self):
        if self.mimonte!=None: 
            return self.mimonte.calcularResultado() 
        else: return 0

    def cambiar_probabilidades(self,probs):
        self.valores_probabilidad_disparo = probs
        self.mimonte = self.mimonte.cambiarProbabilidades(self.valores_probabilidad_disparo)