nome = "Rafael"
idade = 22
profissao = "Desenvolvedor"
linguagem = "Python"
saldo = 39.398

dados = {"nome":"Rafael", "idade":22}

print("Nome: %s, idade: %d" %(nome, idade)) # Desta forma define o tipo de varival com % e passa as varivaies logo após.
print("Nome: {}, idade: {}".format(nome, idade)) # Desta forma define o tipo de varival com {} e passa as varivaies logo após do format.
print("Nome: {0}, idade: {1}".format(nome, idade)) # Desta forma define o tipo de varival com {} e passa as varivaies logo após do format, além de colocar os indices nas chaves.
print("Nome: {nome}, idade: {idade}".format(**dados)) # Desta forma ele vai definir os valores com o que esta no dicionario.
print(f"Nome: {nome}, idade: {idade}") # Desta forma ja define direto, maneira mais facil.

print(f"Nome: {nome}, idade: {idade}, saldo: {saldo:10.2f}") # Para definir o tamanho da variavel saldo, coloca : e 
                                                             # logo após quantos caracteres quer antes do valor e quantas casas decimais serão necessarias.
print(f"Nome: {nome}, idade: {idade}, saldo: {saldo:.2f}")