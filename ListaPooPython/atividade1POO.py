"""

2. Classe Quadrado: Crie uma classe que modele um quadrado:
a. Atributos: Tamanho do lado
b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

"""
class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def mudarValorLado(self, lado):
        self.lado = lado
    
    def retornarValorLado(self):
        return self.lado
    
    def calcularArea(self):
        return self.lado * self.lado




lado1 = Quadrado(float(input('Informe o lado do quadrado: ')))

while True:

    mudar = input('Deseja alterar o valor do lado do Quadrado? [S/N]: ')
    
    if mudar == 's' or mudar == 'sim' or mudar == 'S':

        novo_lado = float(input("Informe o novo valor do lado: "))

        lado1.mudarValorLado(novo_lado)

        print('Novo lado = ' , lado1.retornarValorLado())
    
    else:
        print('Lado do quadrado = ', lado1.retornarValorLado())
    
    calcArea = input('Deseja calcular a area do quadrado? [S/N]: ')

    if calcArea == 's' or calcArea == 'sim' or calcArea == 'S':

        print('A área do quadrado é' , lado1.calcularArea())
    
    else:
        break
        







