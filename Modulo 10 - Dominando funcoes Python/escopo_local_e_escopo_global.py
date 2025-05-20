salario = 2000

def salario_bonus(bonus, lista):
    global salario # No global, ele pega a variavel de fora do escopo e transforma como se fosse um "local"
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(lista_aux)
    salario += bonus
    return salario


lista = [1]
novo_salario = salario_bonus(400, lista)
print(novo_salario)
print(lista)