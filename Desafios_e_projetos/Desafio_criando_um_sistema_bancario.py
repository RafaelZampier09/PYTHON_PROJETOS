# Desafio

'''
Fomos contratados por um grande banco para desenvolver o seu
novo sistema. Esse banco deseja modernizar suas operações e 
para isso escolheu a linguagem Python. Para a primeira versão
do sistema devemos implementar apenas 3 operações:
depósito, saque e extrato
'''

# Operação de deposito
'''
Deve ser possivel depositar valores positivos para a minha
conta bancaria. A v1 do projeto trabalha apenas com 1 usuario,
dessa forma não precisamos nos preocuopar em identificar qual
é o numero da agência e conta bancaria. Todos os depositos devem
ser armaenados em uma variavel e exibidos na operação de extrato
'''

# Operação de saque
'''
O sistema deve permitir realizar 3 saques diarios com limite
maximo de R$500,00 por saque. Caso o usuario não tenha saldo
em conta, o sistema deve exibir uma mensagem informando que não
será possivel sacar o dinheiro por falta de saldo. Todos os 
saques devem ser armazenados em uma variavel e exibidos na 
operação de extrato
'''

# Operação de extrato
'''
Essa operação deve listar todos os depósitos e saques
realizados na conta. No fim da listagem deve ser exibido o 
saldo atual da conta
Os valores devem ser exibidos ultizando o formato R$xxx.xx,
Exemplo:
1500.45 = R$1500.45
'''

import datetime

menu = """

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3
numero_deposito = 1

while True:  
    opcao = input(menu)
    opcao = opcao.lower()

    if opcao == "d":
        
        deposito = float(input("Digite o valor que deseja depositar: R$"))
        
        while deposito < 0:
            deposito = float(input("Digite um valor acima de 0 reais e valido para a operação: R$"))

        saldo += deposito
        hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"{numero_deposito}º deposito de R${deposito:.2f} às {hora}\n"       
        input(f"Deposito de R${deposito:.2f} realizado com sucesso, pressione enter para voltar ao menu...")
        numero_deposito += 1

    elif opcao == "s":

        if saldo <= 0:
            print("Não podemos realizar o saque, não temos saldo suficiante para essa operação.")
            input(f"Pressione enter para voltar ao menu...")
            continue

        if numero_saques >= LIMITE_SAQUE:
            print("Não é possivel efetuar mais saques nessa conta devido ao limite diario de 3.")
            input(f"Pressione enter para voltar ao menu...")
            continue
        
        saque = float(input("Digite o valor que deseja sacar: R$"))

        while saque < 0:
            saque = float(input("Digite um valor acima de 0 reais e valido para a operação: R$"))

        while saque > saldo:
            saque = float(input(f"Digite um valor menor que o saldo de R${saldo:.2f} para saques: R$"))

        while saque > limite:
            saque = float(input("Favor digitar um valor menor que R$500.00 para efetuar o saque: R$"))

        saldo -= saque
        hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"{numero_saques+1}º saque de R${saque:.2f} às {hora}\n" 
        input(f"Saque de R${saque:.2f} realizado com sucesso, pressione enter para voltar ao menu...")      
        numero_saques += 1
        
    elif opcao == "e":
        print("="*30)
        print("EXTRATO BANCARIO".center(30))
        print("="*30)

        if extrato == "":
            print("Sem nenhuma movimentação bancaria até o momento...")
            input(f"Pressione enter para voltar ao menu...")

        else:
            print(extrato)
            print(f"Saldo disponivel: R${saldo:.2f}")
            input(f"Pressione enter para voltar ao menu...")
        
    elif opcao == "q":
        break

    else:
        print("Opção invalida, por favor novamente uma operação valida.")
        