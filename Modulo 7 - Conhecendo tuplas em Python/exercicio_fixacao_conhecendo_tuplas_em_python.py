"""
Exercício – Praticando com Tuplas em Python

Objetivo:
Treinar a criação, acesso e manipulação básica de tuplas.

Descrição:
1. Crie uma tupla chamada `cardapio` com pelo menos 5 itens (ex: 'Pizza', 'Hambúrguer', 'Refrigerante', 'Batata Frita', 'Sobremesa').
2. Exiba todos os itens do cardápio usando um loop.
3. Mostre o primeiro e o último item da tupla.
4. Solicite ao usuário o nome de um item do cardápio que ele deseja.
   - Informe a posição (índice) desse item na tupla (caso exista).
   - Caso não exista, diga que o item não está disponível.
5. Crie uma nova tupla com o cardápio ordenado em ordem alfabética (sem alterar a original).
6. Mostre quantos itens há no cardápio usando `len()`.

Regras:
- Use apenas tuplas (não listas) para armazenar os itens do cardápio.
- Use apenas métodos e recursos compatíveis com tuplas.

Dica:
Tuplas são imutáveis, então você não pode adicionar ou remover itens depois de criá-las.
"""
cardapio = ("Pizza", "Hamburguer", "Refrigerante", "Batata Frita", "Sobremesa")

print("-"*40)
print("Cardapio")
print("")
for indice, item in enumerate(cardapio):
    print(f"{indice} - {item}")

print(f"O primeiro indice: {cardapio[0]}")
print(f"O ultimo indice: {cardapio[-1]}")

item_selecionado = str(input("Informe o item que deseja: ").strip().title())
print(item_selecionado)

if not item_selecionado:
    print("Nenhum item foi selecionado.")
elif item_selecionado not in cardapio:
    print("O item selecionado não esta na lista")
else:
    print(f"O {item_selecionado} esta no indice {cardapio.index(item_selecionado)}")

cardapio_copia = tuple(sorted(cardapio))
print("")
print("Cardapio em ordem alfabetica.")
for indice, item in enumerate(cardapio_copia):
    print(f"{indice} - {item}")
print(f"Temos um total de {len(cardapio_copia)} itens no cardapio.")
