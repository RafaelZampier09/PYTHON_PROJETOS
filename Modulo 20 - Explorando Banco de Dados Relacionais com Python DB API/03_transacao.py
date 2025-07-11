import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute(
        "INSERT INTO clientes (nome, email) VALUES (?,?)",
        ("Teste 1", "teste1@gmail.com"),
    )
    cursor.execute(
        "INSERT INTO clientes (id, nome, email) VALUES (?, ?,?)",
        (3, "Teste 1", "teste1@gmail.com"),
    )
    conexao.commit()
except Exception as exc:
    print(f"OPS! um erro ocorreu! {exc}")
    conexao.rollback()
