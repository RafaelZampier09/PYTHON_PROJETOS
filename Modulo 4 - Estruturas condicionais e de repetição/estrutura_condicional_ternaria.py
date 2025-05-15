saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

# Na condicional ternaria, ele coloca a condição de forma mais compactada.
# Por exemplo, a variavel status tera valor "Sucesso" se saldo for >= a saque, se a expressão foi negatica, ele irá retornar "Falha"

print(f"{status} ao efetuar o saque.")