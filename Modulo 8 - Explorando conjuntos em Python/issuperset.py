conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

print(conjunto_a.issuperset(conjunto_b)) # Retorna falso, pois todos os conjuntos A estão no B
print(conjunto_b.issuperset(conjunto_a)) # Retorna verdade

# No caso do issuperset ele é o contrario do issubset, pois revela se os conjuntos não estão no outro