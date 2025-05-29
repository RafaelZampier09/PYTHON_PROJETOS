def meu_decorador (funcao):
    def envelope():
        print("Faz algo antes de executar")
        funcao()
        print("Faz algo depois de executar")

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Ola mundo {nome}!")


ola_mundo()