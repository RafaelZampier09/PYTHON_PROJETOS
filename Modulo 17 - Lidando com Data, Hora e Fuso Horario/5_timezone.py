from datetime import datetime, timezone, timedelta

data_oslu = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslu)
print(data_sao_paulo)
