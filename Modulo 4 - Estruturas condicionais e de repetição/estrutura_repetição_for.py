texto = input("Informe seu texto: ")
VOGAIS = "AEIOU"


# Exemplo usando um iteravel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print()

# Exemplo usando a função built-in-range
for numero in range (0, 50, 5):
    print(numero)