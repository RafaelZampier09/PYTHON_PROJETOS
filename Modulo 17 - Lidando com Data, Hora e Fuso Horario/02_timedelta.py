from datetime import datetime, timedelta, date, time


tipo_carro = "G" # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(days=tempo_pequeno)
    print(f"O carro chegou: {data_atual}\nFicará pronto aproximadamente: {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(days=tempo_medio)
    print(f"O carro chegou: {data_atual}\nFicará pronto aproximadamente: {data_estimada}")
else:
    data_estimada = data_atual + timedelta(days=tempo_grande)
    print(f"O carro chegou: {data_atual}\nFicará pronto aproximadamente: {data_estimada}")


print(date.today() - timedelta(days=1))
resultado = datetime(2025, 5, 28, 13, 47, 33) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())