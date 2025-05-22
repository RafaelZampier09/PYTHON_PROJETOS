class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        return super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar...")

class Aviao(Passaro):
    def voar(self):
        print("Avião esta decolando")

def plano_de_voo(passaro):
    passaro.voar()

p1 = Pardal()
p2 = Avestruz()
plano_de_voo(p1)
plano_de_voo(p2)

plano_de_voo(Aviao())