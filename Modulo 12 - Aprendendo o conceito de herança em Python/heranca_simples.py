class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor...")

    def __str__(self):
        return self.cor

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado ):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{"Sim" if self.carregado else "Não"} estou carregado")


moto_1 = Motocicleta("Preta", "ABC-1234", 2)
moto_1.ligar_motor()

carro_1 = Carro("Branco", "DEF-5678", 4)
carro_1.ligar_motor()

caminhao_1 = Caminhao("Vermelho", "GHI-9101", 8, False)
caminhao_1.ligar_motor()
caminhao_1.esta_carregado()
print(caminhao_1)