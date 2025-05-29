lista = [1,3,4,6]

class MeuIterador:
    def __init__(self, numeros: list[int]): # Definindo que um dos argumentos tem que ser uma lista
        self.numeros =  numeros
        self.contador = 0

    def __iter__(self):  # Primeiro metodo especial de iteração
        return self
    
    def __next__(self):  # Segundo metodo especial de iteração
        try:
            numero = self.numeros[self.contador]
            if numero % 2 == 0:
                self.contador += 1
                return  numero * 2
            else:
                self.contador += 1
                return numero * 3
            
        except:
            raise StopIteration

for i in MeuIterador(lista):
    print(i)