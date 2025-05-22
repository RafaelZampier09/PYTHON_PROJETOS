class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auau")

    def dormir(self):
        self.acordado = False
        print("Zzzzzzz...")

    def __str__(self):
        return f"{self.__class__.__name__}:{"".join(f'\n{chave} = {valor}' for chave, valor in self.__dict__.items())}"

cao_1 = Cachorro("Madruga", "Preto", False)
cao_2 = Cachorro("Pet", "Branco e preto")

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)
print(cao_2)

        