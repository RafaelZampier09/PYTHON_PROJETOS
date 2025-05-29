from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = '2025-5-28 10:20:30'
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M:%S"

print(data_hora_atual.strftime(mascara_ptbr)) # COnverte uma data para o formato desejado
data_convertida = datetime.strptime(data_hora_str, mascara_en) # Converte uma STR de data em um tipo datetime
print(data_convertida)
print(type(data_convertida))