# Exercício: Sistema de controle de presença com conjuntos

# Objetivo:
# Praticar a criação, modificação e operações com conjuntos em Python.

# Descrição:
# Suponha que você está organizando um evento com duas sessões: Sessão A e Sessão B.
# Você receberá listas com os nomes das pessoas que compareceram a cada sessão.
# Seu trabalho é usar conjuntos para responder às seguintes perguntas:

# 1. Crie dois conjuntos:
#    - Um para os participantes da Sessão A.
#    - Outro para os participantes da Sessão B.

# 2. Mostre:
#    - Quem participou das duas sessões (interseção).
#    - Quem participou de apenas uma das sessões (diferença simétrica).
#    - A lista completa de todos os participantes (união, sem duplicatas).
#    - Quem participou da Sessão A, mas não da B (diferença).
#    - Verifique se os conjuntos são disjuntos (sem nenhum participante em comum).

# Dica:
# Use métodos como .union(), .intersection(), .difference(), .symmetric_difference()
# e o método .isdisjoint() para explorar o que os conjuntos oferecem.

# Extras:
# - Adicione ou remova um nome de um dos conjuntos com .add() e .discard().
# - Mostre quantos participantes únicos houve no total.

conjunto_a = {"Rafael", "Jose", "Daniel", "Barbara", "Leonardo", "Catarina"}
conjunto_b = {"Gilberto", "Leonardo", "Bruna", "Juçara", "Rafael"}

print(f"Os participantes das duas sessôes foram:{conjunto_a.intersection(conjunto_b)} ")
print(f"Os participantes apenas de uma sessão foram:{conjunto_a.symmetric_difference(conjunto_b)}")
print(f"A lista completa de todos os participantes:{conjunto_a.union(conjunto_b)}")
print(f"Os participantes da sessão A que não estavam na sessão B:{conjunto_a.difference(conjunto_b)}")
print(f"Todos os participantes são diferente? {conjunto_a.isdisjoint(conjunto_b)}")

print("")
print("Adicionando uma nova pessoa no conjunto A...")
conjunto_a.add("Marcio")
print("Removendo uma pessoa do conjunto B")
conjunto_b.discard("Bruna")
total_participantes_nao_repetidos = len(conjunto_a.difference(conjunto_b)) + len(conjunto_b.difference(conjunto_a))

print(f"O total de participantes não repetidos é: {total_participantes_nao_repetidos}")