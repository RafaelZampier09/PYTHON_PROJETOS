# 1. Operadores aritmeticos

var_1 = 5
var_2  = 3

print("OPERADORES ARITMETICOS")
print("")
print(f"SOMA: {var_1} + {var_2} = {var_1 + var_2}")
print(f"SUBTRAÇÃO: {var_1} - {var_2} = {var_1 - var_2}")
print(f"MULTIPLICAÇÃO: {var_1} * {var_2} = {var_1 * var_2}")
print(f"DIVISÃO: {var_1} / {var_2} = {var_1 / var_2}")
print(f"MÓDULO DE DIVISÃO: {var_1} % {var_2} = {var_1 % var_2}")
print(f"EXPONENCIAÇÃO: {var_1} ** {var_2} = {var_1 ** var_2}")
print("")
print("*"*60)

# 2. Operadores de atribuição

x = 10
print("")
print("OPERADORES DE ATRIBUIÇÃO")
print("")
x+=3
print(f"ATRIBUIÇÃO COM SOMA DE 3: {x}")
x-=3
print(f"ATRIBUIÇÃO COM SUBTRAÇÃO DE 3: {x}")
x*=2
print(f"ATRIBUIÇÃO COM MULTIPLICAÇÃO DE 2: {x}")
print("")
print("*"*60)

# 3. Operadores logicos

print("")
print("OPERADORES LOGICOS")
print("")
noticia_1 = True
noticia_2 = False
print(f"NOTICIA UM E NOTICIA DOIS SÃO VERDADEIRAS: {noticia_1 and noticia_2}")
print(f"NOTICIA UM OU NOTICIA DOIS SÃO VERDADEIRAS: {noticia_1 or noticia_2}")
print("")
print("*"*60)

# 4. Operadores de identidade

a = 10
b = a
print("")
print("OPERADORES DE IDENTIDADE")
print("")
print(f"A PRIMEIRA VARIAVEL OCUPA O MESMO ESPAÇO DA SEGUNDA VARIAVEL: {a is b}")
print(f"A PRIMEIRA VARIAVEL NÃO OCUPA O MESMO ESPAÇO DA SEGUNDA VARIAVEL: {a is not b}")
print("")
print("*"*60)

# 5. Operadores de associação

print("")
print("OPETRADORES DE ASSOCIAÇÃO")
print("")
frutas = ["maçã", "banana", "laranja"]
print(f"MAÇÃ ESTA DENTRO DE FRUTAS?: {"maçã" in frutas}")
print(f"UVA ESTA DENTRO DE FRUTAS?: {"uva" not in frutas}")
