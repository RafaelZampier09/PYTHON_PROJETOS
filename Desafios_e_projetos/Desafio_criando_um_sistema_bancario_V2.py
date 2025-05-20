# Desafio V2

"""
Objetivo Geral

Separar as funções existentes de saque, depósito e extrato em
funções. Criar duas novas funções: Cadastrar usuário (cliente)
e cadastrar conta bancária.
"""

"""
Desafio

Precisamos deixar nosso código mais modularizado, para isso
vamos criar funções para as operações existentes: sacar,
depositar e vizualizar extrato. Além disso, para a versão 2
do nosso sistema, precisamos criar duas novas funções: Criar
usuário (cliente do banco) e criar conta corrente (vincular com
usuário).
"""

"""
# Separação em funções

Devemos criar funções para todas as operações do sistema. Para
exercitar tudo o que aprendemos neste módulo, cada função vai ter
uma regra na passagem de argumentos. O retorno e a forma como serão
chamadas, pode ser definida por você da forma que achar melhor.
"""

"""
# Saque

A função saque deve receber os argumentos apenas por nome (keyword only).
Sugestão de argumentos: Saldo, valor, extrato, limite, numeros_saques, 
limite_saques. Sugestão de retorno: saldo, extrato
"""

"""
# Depósito

A função deposito deve receber os argumentos apenas por posição
(positional only). Sugestão de argumentos: saldo, valor, extrato.
Sugestão de retorno: saldo e extrato.
"""

"""
# Extrato

A função extrato deve receber os argumentos por posição e
nome (positional only e keyword only). Argumentos posicionais:
saldo, argumentos nomeados: extrato.
"""

"""
# Novas funções

Precisamos criar duas novas funções: Criar usuário e criar conta
corrente. Fique a vontade para adicionar mais funções, exemplo:
listar contas.
"""

"""
# Criar usuário

O programa deve armazenar os usuários em uma lista, um usuário
é composto por: nome, data de nascimento, cpf e endereço. O
endereço é uma string com o formato: logradouro, nro - bairro
cidade/sigla estado. Deve ser armazenado somente os números do CPF
Não podemos cadastrar 2 usuários com o mesmo numero de CPF.
"""

"""
# Criar conta corrente

O programa deve armazenar contas em uma lista, uma conta é 
composta por: agência, número da conta e usuário. O número da conta
é sequencial, iniciando em 1. O número da agência é fixo: "0001". O
usuário pode ter mais de uma conta, mas uma conta pertence somente a
um usuário.
"""

"""
# Dica

Para vincular um usuário a uma conta, filtre a lista de usuários buscando
o número do CPF informado para cada usuário da lista.
"""


import datetime

menu = """

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Criar usuário
[5] - Criar conta
[6] - Listar contas
[7] - Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3
numero_deposito = 1
usuarios = []
contas = []

def depositar(saldo, extrato, numero_deposito,/,):
    while True:
        try:
            deposito = float(input("Digite o valor que deseja depositar: R$"))
            if deposito <= 0:
                print("Valor inválido! O depósito precisa ser maior que zero.")
            else:
                break
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    saldo += deposito
    hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    extrato += f"{numero_deposito}º deposito de R${deposito:.2f} às {hora}\n" 
    input(f"Deposito de R${deposito:.2f} realizado com sucesso, pressione enter para voltar ao menu...")
    numero_deposito += 1
    return saldo, extrato, numero_deposito

def sacar(*,saldo, numero_saques, limite_saque, limite, extrato):
    while True:
        try:

            if saldo <= 0:
                print("Não podemos realizar o saque, não temos saldo suficiente para essa operação.")
                input(f"Pressione enter para voltar ao menu...")
                return saldo, numero_saques, limite_saque, limite, extrato   
                  
            if numero_saques >= limite_saque:

                print("Não é possivel efetuar mais saques nessa conta devido ao limite diario de 3.")
                input(f"Pressione enter para voltar ao menu...")
                return saldo, numero_saques, limite_saque, limite, extrato
            
            saque = float(input("Digite o valor que deseja sacar: R$"))

            if saque <= 0:

                print("Valor inválido! O saque precisa ser maior que zero.")

            elif saque > saldo:

                print("Não é possivel efetuar o saque, não tem esse valor em sua conta...\n")
                continue
            
            elif saque > limite:
                print(f"Valor do saque excede o limite de R${limite:.2f}.\n")
                continue

            else:
                break

        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    saldo -= saque
    hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    extrato += f"{numero_saques+1}º saque de R${saque:.2f} às {hora}\n" 
    input(f"Saque de R${saque:.2f} realizado com sucesso, pressione enter para voltar ao menu...")      
    numero_saques += 1
    return saldo, numero_saques, limite_saque, limite, extrato

def ver_extrato(saldo, / , * , extrato):
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

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")

    # Verifica se o CPF ja existe
    cpf_existe = False
    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            cpf_existe = True
            break

    if cpf_existe:
        print("Ja existe um usuario com esse CPF.")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")

    novo_usuario = {
        "Nome": nome,
        "Data_nascimento":data_nascimento,
        "CPF":cpf,
        "Endereço":endereco
    }

    usuarios.append(novo_usuario)
    print("Usuario cadastrado com sucesso!")
    input(f"Pressione enter para voltar ao menu...")

def criar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuario: ")

    # Procurar usuario com o CPF
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("Usuário não encontrado. Cadastre o usuário antes de criar a conta")
        return
    
    numero_conta = len(contas) + 1
    nova_conta  = {
        "Agência":"0001",
        "Numero":numero_conta,
        "Usuario":usuario_encontrado
    }
    contas.append(nova_conta)
    print(f"Conta criada com sucesso! Agência: 0001 Conta: {numero_conta}")

def listar_contas(contas):
    print("="*40)
    print("LISTA DE CONTAS".center(40))
    print("="*40)

    if not contas:
        print("Nenhuma conta cadastrada até o momento.")

    else:
        for conta in contas:
            print(f"Agência: {conta["Agência"]}")
            print(f"Numero da conta: {conta["Numero"]}")
            print(f"Usuario titular: {conta["Usuario"]["Nome"]}")
            print(f"-"*40)
    input("Pressione enter para voltar ao menu...")

while True:  
    opcao = input(menu)

    if opcao == "1":

        saldo, extrato, numero_deposito = depositar(saldo, extrato, numero_deposito)

    elif opcao == "2":

        saldo, numero_saques, LIMITE_SAQUE, limite, extrato = sacar(saldo=saldo, numero_saques=numero_saques, limite_saque=LIMITE_SAQUE, limite=limite, extrato=extrato)
        
    elif opcao == "3":
        ver_extrato(saldo, extrato=extrato)
        
    elif opcao == "4":
        criar_usuario(usuarios)
        
    elif opcao == "5":
        criar_conta(contas, usuarios)
        
    elif opcao == "6":
        listar_contas(contas)
        
    elif opcao == "7":
        break

    else:
        print("Opção invalida, por favor novamente uma operação valida.")
        