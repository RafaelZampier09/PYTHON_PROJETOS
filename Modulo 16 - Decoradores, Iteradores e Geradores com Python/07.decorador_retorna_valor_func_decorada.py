def meu_decorador (funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de executar")
        return resultado
    
    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Ola mundo {nome}!")
    return nome.upper()


result = ola_mundo("Rafael")
print(result)