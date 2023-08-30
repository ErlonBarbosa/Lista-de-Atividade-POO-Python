class Bola():
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    
    def mostrarCor(self):
        return self.cor


bola1 = Bola('Azul', 20, 'couro')
print(bola1.mostrarCor())
print()

while True:

    alterar = input('Deseja alterar a cor? [s/n]: ')

    if alterar == 's' or alterar == 'sim' or alterar == 'S':
        
        nova_cor = input('Inoforme a cor: ')
        bola1.trocaCor(nova_cor)
        print(bola1.mostrarCor())

    else:

        print(bola1.mostrarCor())
        break




