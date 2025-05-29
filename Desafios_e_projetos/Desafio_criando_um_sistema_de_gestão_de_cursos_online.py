'''
# 📚 Sistema de Gestão de Cursos Online

# 1. Classe Abstrata: Pessoa
# ---------------------------
# Atributos:
# - nome
# - email
#
# Métodos:
# - exibir_dados() → método abstrato que deve ser implementado pelas subclasses


# 2. Subclasses de Pessoa:
# =========================

# ✅ Classe Aluno
# ----------------
# Atributos:
# - lista de cursos matriculados (ex: self.cursos_matriculados)
#
# Métodos:
# - matricular(curso) → adiciona um curso à lista de cursos
# - exibir_dados() → exibe nome e email
# - listar_cursos() → exibe todos os cursos em que o aluno está matriculado


# ✅ Classe Instrutor
# -------------------
# Atributos:
# - área de especialização (ex: self.especializacao)
# - cursos ministrados (ex: self.cursos_ministrados)
#
# Métodos:
# - atribuir_curso(curso) → adiciona um curso à lista de cursos ministrados
# - exibir_dados() → exibe nome, email e especialização
# - listar_cursos_ministrados() → exibe todos os cursos atribuídos ao instrutor


# 3. Classe Curso
# ---------------
# Atributos:
# - titulo
# - descricao
# - instrutor (objeto da classe Instrutor)
#
# Métodos:
# - exibir_informacoes() → mostra os dados do curso e nome do instrutor

'''

from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email
    
    @abstractmethod
    def exibir_dados(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, email):
        super().__init__(nome, email)
        self.cursos_matriculados = []

    def matricular (self, curso):
        self.cursos_matriculados.append(curso)
        print(f"{self.nome} foi matriculado no curso: {curso.titulo}")

    def exibir_dados(self):       
        print(f"\nNome: {self.nome} | Email: {self.email}")

    def exibir_cursos(self):
        if not self.cursos_matriculados:
            print("\nNenhum curso matriculado até o momento...")
        else:
            print("\nCursos matriculados: ")
            for curso in self.cursos_matriculados:
                print(f"- {curso.titulo}")

class Instrutor(Pessoa):
    def __init__(self, nome, email, especializacao):
        super().__init__(nome, email)
        self._especializacao = especializacao
        self.cursos_ministrados = []

    @property
    def especializacao(self):
        return self._especializacao
    
    def atribuir_curso(self, curso):
        self.cursos_ministrados.append(curso)
        print(f"{self.nome} agora ministra o curso: {curso.titulo}")

    def exibir_dados(self):
        print(f"Nome: {self.nome} | Email: {self.email} | Especialização: {self.especializacao}")

    def listar_cursos_ministrados(self):
        if not self.cursos_ministrados:
            print("\nNenhum curso ministrado até o momento...")
        else:
            print("\nCursos ministrados: ")
            for curso in self.cursos_ministrados:
                print(f"- {curso.titulo}")


class Curso:
    def __init__(self, titulo, descricao, instrutor):
        self.titulo = titulo
        self.descricao = descricao
        self.instrutor = instrutor

    def exibir_informacoes(self):
        print(f"\nCurso: {self.titulo}\nDescrição: {self.descricao}\nInstrutor: {self.instrutor.nome}")



aluno1 = Aluno("Rafael Zampier", "rafaelzampier14@gmail.com")
instrutor1 = Instrutor("Jose Carlos", "josecarlos22@gmail.com", "Informatica")

curso1 = Curso("Python para iniciantes", "Aprenda com os fundamentos de Python", instrutor1)

instrutor1.atribuir_curso(curso1)
aluno1.matricular(curso1)

aluno1.exibir_cursos()
instrutor1.listar_cursos_ministrados()
curso1.exibir_informacoes()
        



    

