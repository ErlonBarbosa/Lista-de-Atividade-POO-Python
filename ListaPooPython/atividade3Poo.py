"""
3. Classe Retângulo: Crie uma classe que modele um retângulo:
a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura,
a escolher)
b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área
e calcular Perímetro;
c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que
informe as medidas de um local. Depois, deve criar um objeto com as
medidas e calcular a quantidade de pisos e de rodapés necessárias para
o local.
"""

class Retangulo:

    def __init__(self, base, altura):

        self.base = base
        self.altura = altura
    
    def mudarValorLados(self, base, altura):
        
        self.base = base
        self.base = altura
    
    def retornarValorLados(self, base, altura):
        
        self.base = base
        self.base = altura

    def calcArea(self):
        return self.base * self.altura
    
    def calcPerimetro(self):
        return 2 * (self.base + self.altura)
    

def main():

    comprimento = float(input("Informe o comprimento do local: "))
    largura = float(input("Informe a largura do local: "))
    
    retangulo = Retangulo(comprimento, largura)

    area = retangulo.calcArea()
    perimetro = retangulo.calcPerimetro()

    print(f"Área do local: {area} metros quadrados")
    print(f"Perímetro do local: {perimetro} metros")

    tamanho_piso = float(input("Informe o tamanho de um piso: "))
    tamanho_rodape = float(input("Informe o tamanho de um rodapé: "))

    quantidade_pisos = area / tamanho_piso
    quantidade_rodapes = 2 * (comprimento + largura) / tamanho_rodape

    print(f"Quantidade de pisos necessários: {quantidade_pisos:.2f}")
    print(f"Quantidade de rodapés necessários: {quantidade_rodapes:.2f}")

if __name__ == "__main__":
    main()

    

