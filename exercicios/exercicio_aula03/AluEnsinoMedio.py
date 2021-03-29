
from algoritmo_programacao_II.exercicios.exercicio_aula03.Aluno import Aluno


class AluEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        print("Código: ", self.codigo, "\nNome: ", self.nome, "\nMatricula: ", self.matricula, "\nAno: ", self.ano)
