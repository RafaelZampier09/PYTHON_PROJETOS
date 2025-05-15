MAIOR_DE_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

# Apenas IF
print("-"*60)
print("Exemplo apenas com IF")
if idade >= MAIOR_DE_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_DE_IDADE:
    print("Não pode tirar a CNH, menor de idade.")


# If/Else
print("-"*60)
print("Exemplo com If/Else")
if idade >= MAIOR_DE_IDADE:
    print("Maior de idade, pode tirar a CNH.")

else:
    print("Não pode tirar a CNH, menor de idade.")


#If/Else/Elif
print("-"*60)
print("Exemplo com If/Elif/Else")
if idade >= MAIOR_DE_IDADE:
    print("Maior de idade, pode tirar a CNH.")

elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas praticas.")

else:
    print("Não pode tirar a CNH, menor de idade.")
print("-"*60)

