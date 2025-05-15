# Programa que simula um caixa eletronico simples desenvolvido em python

saldo_inicial = 1000
opcao = -1

while opcao != 3:
    valor_sacado = 0
    opcao = int(input("[1] Ver saldo\n[2] Sacar valor\n[3] Sair\n"))
    if opcao == 1:
        print(f"Saldo disponivel: R${saldo_inicial}")
    
    if opcao == 2:
        valor_sacado = float(input("Digite o valor que deseja sacar: "))
        if valor_sacado > saldo_inicial:
            print("Saldo induficiente...")
        
        else:
            saldo_inicial -= valor_sacado
            print(f"Saque realizado. Novo saldo: R${saldo_inicial}")
else:
    print("Encerrando... Obrigado por usar nosso sistema.")
