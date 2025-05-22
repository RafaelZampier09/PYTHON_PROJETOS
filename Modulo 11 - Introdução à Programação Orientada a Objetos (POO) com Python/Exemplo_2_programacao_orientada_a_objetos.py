class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1

    def buzinar(self):
        print("Plim Plim")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada.")

    def correr(self):
        print("Vruuum")
    
    def get_cor(self):
        return self.cor

    def __str__(self):
        return f"{self.__class__.__name__}:{"".join([f'\n{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    
    
b1 = Bicicleta("Preto", "Caloi", 2017, 2.400)
b1.buzinar()
b1.parar()
b1.correr()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Marrom", "Monark", 2019, 200)
b2.buzinar()   # Bicicleta.buzinar(b2)
print(b2.get_cor())
print(b2)