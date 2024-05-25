import riManage

class LineasEspera():
    def __init__(self):
        self.resultado = None
        self.manejoRi = riManage.riManage()
        self.manejoRi.generarNumerosHastaPasarPruebas(100000)

    def caminar(self,min,max):
        lista_inicial = self.manejoRi.ObtenerCantidadRi(10000)# numeros decimales
        lista_IAT = []# enteros en segundos 
        lista_IAAT = []
        for i in range(len(lista_inicial)):
            #(10000 + (30000 - 10000)
            valor = int((min + (max - min)) * lista_inicial[i])# genera numeros enteros uniformes
            lista_IAT.append(valor)
         
        lista_IAAT.append(lista_IAT[0]) #primer valor de lista IAAT
          
        for i in range(len(lista_IAT) - 1):
            lista_IAAT.append(lista_IAAT[i] + lista_IAT[i + 1])
              
        return lista_IAAT
    

        

   
    