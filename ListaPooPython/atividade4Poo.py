"""
4. Classe Pessoa: Crie uma classe que modele uma pessoa:
a. Atributos: nome, idade, peso e altura
b. Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão,
a cada ano que nossa pessoa envelhece, sendo a idade dela menor que
21 anos, ela deve crescer 0,5 cm.
"""

class pessoa:

    def __init__(self, nome, idade, peso, altura):
        
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, anos):
        self.idade += anos

        if self.idade < 21:
            self.crescer(0.5 * anos)
    
    def engordar(self, ganhoPeso):
        self.peso += ganhoPeso
        
    def emagrecer(self, perdaPeso):
        self.peso -= perdaPeso
        
    def crescer(self, ganhoAltura):
        self.altura += ganhoAltura

nome = input('Informe o seu nome: ')
idade = int(input('Informe a sua idade: '))
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))

Pessoa = pessoa(nome, idade, peso, altura)

envelheceu = int(input('Informe quantos anos envelheceu: '))
Pessoa.envelhecer(envelheceu)
print(f"Altura após envelhecer: {Pessoa.altura} cm")
print(f"Idade após envelhecer: {Pessoa.idade} anos")

engordou = float(input('Informe quantos kg engordou: '))
Pessoa.engordar(engordou)
print(f"Peso após engordar: {Pessoa.peso} kg")

emagreceu = float(input('Informe quantos kg emagreceu: '))
Pessoa.emagrecer(emagreceu)
print(f"Peso após emagrecer: {Pessoa.peso} kg")









