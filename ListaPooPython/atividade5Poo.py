
"""
5. Classe Conta Corrente: Crie uma classe para implementar uma conta
corrente. A classe deve possuir os seguintes atributos: número da conta, nome
do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e
saque; No construtor, saldo é opcional, com valor default zero e os demais
atributos são obrigatórios.

"""

class ContaCorrente:
    
    def __init__(self, numeroConta, nome, valor):
        self.numeroConta = numeroConta
        self.nome = nome
        self.valor = valor
    
    def alterarnome(self, novoNome):
        self.nome = novoNome
    
    def deposito(self, novoValor):
        self.valor += novoValor
    
    def saque(self, retiradaValor):
        self.valor -= retiradaValor




print('CONTA CORRENTE')
print()
conta = int(input("informe o numero da conta: "))
nome = input('Informe o nome do titular da conta: ')



opcao1 = input("Deseja iniciar a conta fazendo um déposito? [s/n]:  ")


if opcao1 == 's' or opcao1 == 'sim' or opcao1 == 'S':
    novoValor = float(input('Valor a ser depositado R$: '))
    conta1 = ContaCorrente(conta, nome, novoValor)
    print()
    print('Informações da conta!!')
    print(f'Conta: {conta1.numeroConta}')
    print(f'Titular da conta: {conta1.nome}')
    print(f'Saldo em conta: {novoValor}')

else:
    print('Informações da conta!!')
    print(f'Conta: {conta1.numeroConta}')
    print(f'Titular da conta: {conta1.nome}')
    print(f'Saldo = R$ 00,00')

while True:
    
    opcao2 = input("Deseja efetuar um novo deposito? [s/n]: ")

    if opcao2 == 's' or opcao2 == 'sim' or opcao2 == 'S':
        novoValor = float(input('Valor a ser depositado R$: '))
        conta1.deposito(novoValor)
        print()
        print('Informações da conta!!')
        print(f'Conta: {conta1.numeroConta}')
        print(f'Titular da conta: {conta1.nome}')
        print(f'Saldo em conta: {conta1.valor}')
        
    else:
        print('Informações da conta!!')
        print(f'Conta: {conta1.numeroConta}')
        print(f'Titular da conta: {conta1.nome}')
        print(f'Saldo = {novoValor}')
        
    opcao3 = input("Deseja efetuar uma retirada? [s/n]: ")

    if opcao3 == 's' or opcao3 == 'sim' or opcao3 == 'S':
        retirada = float(input('Valor da retirada R$: '))
        conta1.saque(retirada)
        print()
        print('Informações da conta!!')
        print(f'Conta: {conta1.numeroConta}')
        print(f'Titular da conta: {conta1.nome}')
        print(f'Saldo em conta: {conta1.valor}')
    else:
        print('Informações da conta!!')
        print(f'Conta: {conta1.numeroConta}')
        print(f'Titular da conta: {conta1.nome}')
        print(f'Saldo = {conta1.valor}')
    
    opcao4 = input("Deseja alterar o nome? [s/n]: ")

    if opcao4 == 's' or opcao4 == 'sim' or opcao4 == 'S':
        novoNome = input('Novo nome: ')
        conta1.alterarnome(novoNome)
        print()
        print('Informações da conta!!')
        print(f'Conta: {conta1.numeroConta}')
        print(f'Titular da conta: {conta1.nome}')
        print(f'Saldo em conta: {conta1.valor}')
    else:
        print('Informações da conta!!')
        print(f'Conta: {conta1.numeroConta}')
        print(f'Titular da conta: {conta1.nome}')
        print(f'Saldo = {conta1.valor}')



    
    

        
        