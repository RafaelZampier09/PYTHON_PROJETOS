def criar_carro(modelo, ano, placa, / , marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Flex") # Valido
# criar_carro(modelo="Palio",ano=1999,placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Flex") # Invalido

def exemplo (a, /, b, *, c): # Antes do / só posso passar valor, depois do * só posso passar por nome, entre os dois posso passar ambos
    print(a, b, c)

exemplo(10, 11, c=12)
exemplo(10, b=11, c=12)