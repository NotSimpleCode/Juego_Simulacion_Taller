#import riManage



class MarkovClass():
    def __init__(self,dict_nombre_estados,montecarlosProbabilidades):
        self.estado_actual = 1
        self.probs = montecarlosProbabilidades
        self.diccionario_estados = dict_nombre_estados
        self.montecarloActual = None
        

    def obtenerSiguienteEstado(self):
        self.montecarloActual = self.probs[self.estado_actual]
        resultado = self.montecarloActual.calcularResultado()
        self.estado_actual = resultado
        return resultado

    def obtenerNombreEstado(self):
        return self.diccionario_estados[self.estado_actual]

"""
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
"""
def run(estados_nombres,montecarlosProbs):
    markov = MarkovClass(estados_nombres,montecarlosProbs)
    return markov
    """
    for i in range (1000):
        print(markov.obtenerSiguienteEstado())
        print(markov.obtenerNombreEstado())
    """

#run()



