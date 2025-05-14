saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(saldo >= saque and saque <= limite) # Operador "e" (and) - Todos devem ser verdades

print(saldo >= saque or saque <= limite) # Operador "ou" (or) - Um deve ser verdade

print(not saldo > saque) # Operador de negação "não" (not) - Verifica se a condição é falsa, ou seja, ele é ao contrario da verdade

ex1 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(ex1)