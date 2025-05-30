import csv
from pathlib import Path
COLUNA_ID = 0
COLUNA_NOME = 1
ROOT_PATH = Path(__file__).parent
# try:
#     with open(ROOT_PATH / "usuarios.csv", "w",newline ="", encoding="utf-8") as arquivo:
#         escritor = csv.writer(arquivo)
#         escritor.writerow(["id","Nome"])
#         escritor.writerow(["1","Rafael"])
#         escritor.writerow(["2","Barbara"])
# except PermissionError as exc:
#     print(f"Não foi possivel abrir o arquivo: {exc}")

# try:
#     with open(ROOT_PATH / "usuarios.csv", "r", encoding="utf-8") as arquivo:
#         leitor = csv.reader(arquivo)
#         for row in leitor:
#             print(row)
# except PermissionError as exc:
#     print(f"Não foi possivel abrir o arquivo: {exc}")

# try:
#     with open(ROOT_PATH / "usuarios.csv", "r",newline="", encoding="utf-8") as arquivo:
#         leitor = csv.reader(arquivo)
#         for idx, row in enumerate(leitor):
#             if idx == 0:
#                 continue
#             print(f"ID: {row[COLUNA_ID]}")
#             print(f"Nome: {row[COLUNA_NOME]}")
# except PermissionError as exc:
#     print(f"Não foi possivel abrir o arquivo: {exc}")

try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        reader = csv.DictReader(arquivo)
        for row in reader:
            print(f"ID: {row["id"]}")
            print(f"Nome: {row["Nome"]}")
            print("-"*30)
except PermissionError as exc:
    print(f"Não foi possivel abrir o arquivo: {exc}")