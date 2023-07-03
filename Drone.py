from Veiculo import Veiculo

class Drone(Veiculo):
    def __init__(self, marca, modelo, qtdHelices):
        super().__init__(marca, modelo)
        self.__qtdHelices = qtdHelices

    def getQtdHelices(self):
        return self.__qtdHelices

    def setQtdHelices(self, qtdHelices):
        self.__qtdHelices = qtdHelices

    def imprimir(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Quantidade de Hélices: ", self.__qtdHelices)
