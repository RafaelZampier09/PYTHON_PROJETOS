contatos = {
    "rafaelzampier14@gmail.com":{"Nome":"Rafael", "Sobrenome":"Zampier", "Idade": "22"},
    "josesilva@gmail.com":{"Nome":"Jose", "Sobrenome":"Silva", "Idade": "33"}
}

resultado = contatos.get("chave")
print(resultado)

resultado = contatos.get("chave", {}) # Aqui se caso não tiver a chave, ele irá  retornar um valor default
print(resultado)

resultado = contatos.get("rafaelzampier14@gmail.com", {}) #Aqui foi encontrado a chave
print(resultado) 


resultado


# O get serve como uma segunda forma de se obter o valor de uma chave
# Caso uma chave não existir, ele irá retornar none e não dar como erro