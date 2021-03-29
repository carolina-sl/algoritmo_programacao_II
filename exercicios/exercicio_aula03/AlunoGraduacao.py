
from algoritmo_programacao_II.exercicios.exercicio_aula03.Aluno import Aluno


class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        print("Código: ", self.codigo, "\nNome: ", self.nome, "\nMatrícula: ", self.matricula,
              "\nSemestre: ", self.semestre)
