from Veiculo import Veiculo 
from Drone import Drone
from Carro import Carro

class Pilha:
    def __init__(self):
        self.__lista = []

    def push(self, veiculo):
        self.__lista.append(veiculo)

    def pop(self):
        if not self.isEmpty():
            return self.__lista.pop()

    def isEmpty(self):
        return len(self.__lista) == 0

    def imprimir(self):
        for veiculo in self.__lista:
            veiculo.imprimir()

class Main:
    def __init__(self):
        self.__pilhaCarros = Pilha()
        self.__pilhaDrones = Pilha()

    def main(self):
        while True:
            print("1 - Adicionar Carro")
            print("2 - Remover Carro")
            print("3 - Adicionar Drone")
            print("4 - Remover Drone")
            print("5 - Imprimir Pilha de Carros")
            print("6 - Imprimir Pilha de Drones")
            print("0 - Sair")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                marca = input("Digite a marca do carro: ")
                modelo = input("Digite o modelo do carro: ")
                portas = int(input("Digite a quantidade de portas do carro: "))
                carro = Carro(marca, modelo, portas)
                self.__pilhaCarros.push(carro)
            elif opcao == 2:
                self.__pilhaCarros.pop()
            elif opcao == 3:
                marca = input("Digite a marca do drone: ")
                modelo = input("Digite o modelo do drone: ")
                qtdHelices = int(input("Digite a quantidade de hélices do drone: "))
                drone = Drone(marca, modelo, qtdHelices)
                self.__pilhaDrones.push(drone)
            elif opcao == 4:
                self.__pilhaDrones.pop()
            elif opcao == 5:
                self.__pilhaCarros.imprimir()
            elif opcao == 6:
                self.__pilhaDrones.imprimir()
            elif opcao == 0:
                break

menu = Main()
menu.main()
