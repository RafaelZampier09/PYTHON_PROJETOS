import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input("Digite o id do cliente: ")
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")
cliente = cursor.fetchone()
print(dict(cliente))
