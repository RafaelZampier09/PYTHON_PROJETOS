def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1122") # Posso passar a função apenas chamando os valores em sequencia
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1122") # Posso chamar passando o conjunto chave e valor
salvar_carro(**{"marca":"Fiat", "modelo":"Palio", "ano":1999, "placa":"ABC-1122"}) # Esses dois asteriscos no começo, quer dizer que estou passando um dicionario para essa função