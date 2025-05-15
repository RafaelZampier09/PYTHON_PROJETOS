
while True:
    numero = int(input("Informe um numero: "))

    if numero == 10:
        break

    print(numero)


for numero in range (100):
    if numero == 12:
        continue # Ele ira exibir todos os numeros, menos o 12

    print(numero, end=" ")