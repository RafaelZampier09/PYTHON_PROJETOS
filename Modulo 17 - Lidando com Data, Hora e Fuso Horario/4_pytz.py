import pytz
from datetime import datetime

data = datetime.now(pytz.timezone("America/Boise"))
data2 = datetime.now(pytz.timezone("America/Boa_Vista"))
mascara_ptbr = "%H:%M:%S"
print(data.strftime(mascara_ptbr))
print(f"Horario em Roraima: {data2.strftime(mascara_ptbr)}")