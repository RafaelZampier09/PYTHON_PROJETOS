sorteio = {1, 23}

sorteio.add(25)
print(sorteio)
sorteio.add(42)
print(sorteio)
sorteio.add(25) # Aqui não ira adicionar pois ja existe um 25 dentro do conjunto
print(sorteio)

# O add ele ira adicionar um valor caso esse valor não exista n o conjunto