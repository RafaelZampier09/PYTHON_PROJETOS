'''
Exercício 2 – Herança Múltipla
Crie um sistema que represente veículos aquáticos e terrestres.

Requisitos:
Crie a classe Veiculo com:

Atributos: marca, modelo

Método: exibir_dados()

Crie a classe Aquatico com:

Método: navegar(), que imprime algo como “Navegando nas águas...”

Crie a classe Terrestre com:

Método: dirigir(), que imprime algo como “Dirigindo na estrada...”

Crie a classe Anfibio que herda de Aquatico, Terrestre e Veiculo:

Adicione um método que chame navegar() e dirigir().

Crie uma instância de Anfibio e:

Mostre os dados do veículo

Execute os métodos de navegação e direção
'''

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Aquatico(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def navegar(self):
        print("Navegando nas aguas...")

class Terrestre(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def dirigir(self):
        print("Andando na estrada...")

class Hibrido(Aquatico, Terrestre):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def __str__(self):
        return f"{self.__class__.__name__}:{"".join(f'\n{chave} = {valor}' for chave, valor in self.__dict__.items())}"
    

carro_aquatico = Hibrido("BYD", "Yangwang U8")
print(carro_aquatico)
carro_aquatico.navegar()
carro_aquatico.dirigir()