'''
Exercício: Conta Bancária
Objetivo:
Criar uma classe que representa uma conta bancária, controlando saldo com encapsulamento e utilizando @property para acessar e modificar dados com regras.

Requisitos:
Crie uma classe chamada ContaBancaria

Ela deve ter os seguintes atributos:

titular (nome do dono da conta)

_saldo (valor inicial da conta, encapsulado)

Implemente:

Um método depositar(valor) que soma ao saldo

Um método sacar(valor) que subtrai do saldo, mas só se houver saldo suficiente

Use a propriedade saldo com:

Um @property para acessar o saldo

Um @saldo.setter para impedir que o saldo seja definido diretamente (mostre uma mensagem de erro, por exemplo)
'''

class ContaBancaria():
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo or 0
    
    @saldo.setter
    def saldo(self, valor):
        print ("Proibido acessar desta forma")

# Com o property e o setter, eu permito que o saldo seja acessado apenas de forma como getter, mas não deixe o usuario alterar diretamente os processos
    
    def depositar(self, valor_depoito):
        if valor_depoito > 0:
            self._saldo += valor_depoito
            print(f"Deposito de R${valor_depoito:.2f} realizado com sucesso!")
        else:
            print("Valor invalido para deposito")

    def sacar(self, valor_saque):
        if valor_saque <= self._saldo:
            self._saldo -= valor_saque
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
        elif valor_saque <= 0:
            print("Valor invalido para sacar...")
        else:
            print("Saldo insuficiente para saque...")

conta_1 = ContaBancaria("Rafael", 1000)

print(conta_1.saldo)
conta_1.depositar(400)
print(conta_1.saldo)
conta_1.sacar(500)
print(conta_1.saldo)
conta_1.sacar(2000)
conta_1.sacar(100)
print(conta_1.saldo)

conta_1.saldo = 99999

