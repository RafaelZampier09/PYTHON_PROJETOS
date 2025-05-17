conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b)) # Aqui sera verdade, pois nenhum item de A esta contido em B 
print(conjunto_a.isdisjoint(conjunto_c)) # Aqui sera falso, pois temos item de A contidos em B

# Isdisjoint revela se não tem algum item no outro conjuntos