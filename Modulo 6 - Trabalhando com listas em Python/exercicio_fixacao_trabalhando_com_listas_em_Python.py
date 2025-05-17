# ============================================================
# Exercício – Gerenciador de Playlist Musical 🎵
# 
# Objetivo: Praticar os seguintes conceitos de listas em Python:
# - Criação e acesso a dados
# - Métodos da classe list
#
# Instruções:
# 1. Crie uma lista vazia chamada `playlist`.
# 2. Adicione pelo menos 5 músicas à playlist usando dois métodos diferentes
#    (como append(), extend() ou insert()).
# 3. Mostre:
#    - A primeira e a última música usando índices positivos e negativos.
#    - As três primeiras músicas usando fatiamento.
#    - Uma cópia da playlist em ordem alfabética (sem alterar a original).
# 4. Peça ao usuário o nome de uma música:
#    - Se ela estiver na playlist, mostre sua posição (index()) e remova (remove()).
#    - Se não estiver, adicione na segunda posição (insert(1, ...)).
# 5. Conte quantas músicas da playlist começam com a letra "A" ou "a".
# 6. Ordene a playlist em ordem alfabética usando sort() e exiba o resultado.
# 7. Limpe a playlist usando clear() e mostre que ela está vazia.
#
# Métodos que devem ser usados:
# - append()
# - extend()
# - insert()
# - index()
# - remove()
# - sort()
# - clear()
#
# Dica: use if/else, in, e fatiamento de listas.
# ============================================================

playlist =  []

playlist.append("2 Corinthians 5:7")
playlist.append("Poesia Acustica 2")
playlist.append("Peita do Coringão")
playlist.extend(["Ele Quer Ser Eu", "Vou Ter Que Superar"])

# Mostrando para o usario a playlist
print("Playlist criada!")
print(f"Primeira musica: {playlist[0]}")
print(f"Ultima musica: {playlist[-1]}")
print(f"Top 3:{playlist[:3]}")
playlist_copia = playlist.copy()
playlist_copia.sort()
print(f"Playlist (copia) em ordem alfabética: {playlist_copia}")
print("-"*30)


# Pedindo ao usuario o nome de uma musica
musica_desejada = str(input("Qual musica deseja buscar? "))
if not musica_desejada.strip():
    print("Você não digitou nenhuma musica.")
else:
    if musica_desejada in playlist:
        print(f"A musica {musica_desejada} está na posição {playlist.index(musica_desejada)}. Removendo...")
        playlist.remove(musica_desejada)
    else:
        print(f"A musica {musica_desejada} não esta na lista. Vamos adiciona-la...")
        playlist.insert(1, musica_desejada.title())

# Musicas com a letra A
print("-"*30)
playlist_com_a = [musica for musica in playlist if musica.strip().lower().startswith("a")]
print(f"Numero de musicas que comecem com a letra 'A': {len(playlist_com_a)}")

# Ordem alfabetica usando sort
playlist.sort()
print(f"Playlist ordernada: {playlist}")

# Limpando a playlist
print("Limpando a playlist...")
playlist.clear()
print(f"Playlist vazia? {len(playlist)==0}")



