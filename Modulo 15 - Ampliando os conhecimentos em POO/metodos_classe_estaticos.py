class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        print(cls)
        idade = 2022 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_de_dade(idade):
        return idade >= 18


# p = Pessoa("Rafael", 22)
# print(p.nome, p.idade)

p2 = Pessoa.criar_de_data_nascimento(2002, 12, 14, "Jose")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_de_dade(p2.idade))
print(Pessoa.e_maior_de_dade(17))