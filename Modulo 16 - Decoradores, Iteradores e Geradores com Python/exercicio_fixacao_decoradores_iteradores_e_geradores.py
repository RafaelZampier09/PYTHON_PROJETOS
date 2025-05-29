"""
Sistema de Processamento de Tarefas com Log

Este programa simula o processamento de uma fila de tarefas utilizando conceitos de:
- Iteradores personalizados: para percorrer uma lista de tarefas.
- Geradores: para simular a execução de cada tarefa em etapas (ex: Início, Processamento, Fim).
- Decoradores: para registrar logs antes e depois da execução de cada tarefa.

O objetivo é consolidar o entendimento prático sobre esses três tópicos ao mesmo tempo,
criando um fluxo de trabalho assíncrono e monitorado por logs.

Exemplo de execução esperada:
Executando: Backup
Iniciando Backup
Processando Backup
Finalizando Backup
Finalizou: Backup

Executando: Atualização
...

Desafios adicionais:
- Adaptar o gerador para receber tarefas com tempos diferentes.
- Estender o decorador para calcular o tempo total de execução da tarefa.
"""
import functools

tarefas = ["Backup", "Atualização", "Limpeza", "Checkup"]

class FilaTarefas:
    def __init__(self, tarefas): # Armazena as tarefas e inicializa um contador para iterar sobre elas
        self.tarefas = tarefas
        self.contador = 0

    def __iter__(self): # Torna a instancia da classe iteravel. Retorna a si mesma como um iterador
        return self

    def __next__(self): # Cada chamada retorna a proxima tarefa da lista
        if self.contador < len(self.tarefas):
            tarefa = self.tarefas[self.contador]
            self.contador += 1
            return tarefa
        else:
            raise StopIteration # Quando todas as tarefas forem retornadas, é disparado encerrando o for
        
def log_execucao(funcao): # Função de decorador, modifica o comportamento de outra
    @functools.wraps(funcao) # Garante que a função decorada mantanha nome, docstring, etc
    def executar(*args, **kwargs):
        nome = args[0]
        print(f"[LOG] Iniciando a execução de: {nome}")
        for resultado in funcao(*args, **kwargs):
            yield resultado
        print(f"[LOG] Finalizando a execução de: {nome}\n")
        return resultado
    return executar


@log_execucao # exibe logs antes e depois de ser executada
def executar_tarefa(tarefa): # Recebe uma tarefa e simula as etapas da simulação
    yield f"Executando: {tarefa}"
    yield f"Iniciando {tarefa}"
    yield f"Processando {tarefa}"
    yield f"Finalizando {tarefa}"
    yield f"Finalizou: {tarefa}"

fila = FilaTarefas(tarefas)

for tarefa_nome in fila:
    for etapa in executar_tarefa(tarefa_nome):
        print(etapa)

