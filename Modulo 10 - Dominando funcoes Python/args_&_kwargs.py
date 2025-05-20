# def exibir_poema (data_extenso, *lista, **dicionario):
#     texto = "\n".join(lista)
#     meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in dicionario.items()])
#     mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
#     print(mensagem)


# exibir_poema("Segunda-Feira, 19 de maio de 2025","Zen of Python", "Beautiful is batter than ugly.", autor="Tim Peters", ano=1999)

def exibir(*args, **kwargs):
    for indice, valor in enumerate(args):
        print(f"{indice} - {valor}")
    print(type(args))
    print("-"*30)
    for chave, item in kwargs.items():
        print(f"{chave}:{item}")
    print(type(kwargs))

exibir("Jose", 23, nome="Rafael", idade=23)

# No args eu posso passar varios valores que não forem nomeados, onde sera convertido em tupla
# No Kwargs eu posso passar varios valores mas tenho que definir, onde sera convertido em dicionario