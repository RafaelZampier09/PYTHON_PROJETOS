class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}:{"".join(f'\n{chave} = {valor}' for chave, valor in self.__dict__.items())}"

class Mamifero(Animal):
    def __init__(self, cor_do_pelo, **kw):
        super().__init__(**kw)
        self.cor_do_pelo = cor_do_pelo


class Ave(Animal):
    def __init__(self, cor_do_bico, **kw):
        super().__init__(**kw)
        self.cor_do_bico = cor_do_bico

# class Ornitorrinco(Mamifero, Ave):
#     def __init__(self, cor_do_bico, cor_do_pelo, numero_patas):
#         super().__init__(cor_do_bico=cor_do_bico, cor_do_pelo=cor_do_pelo, numero_patas=numero_patas)

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, **kw):
        super().__init__(**kw)

ornitorrinco = Ornitorrinco(numero_patas=2, cor_do_pelo="Verde", cor_do_bico = "Marrom")
print(f"\n{ornitorrinco}")