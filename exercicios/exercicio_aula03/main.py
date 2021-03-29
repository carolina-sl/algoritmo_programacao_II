
from algoritmo_programacao_II.exercicios.exercicio_aula03.Aluno import Aluno
from algoritmo_programacao_II.exercicios.exercicio_aula03.AluEnsinoMedio import AluEnsinoMedio
from algoritmo_programacao_II.exercicios.exercicio_aula03.AlunoGraduacao import AlunoGraduacao

aluno = Aluno(1, "Carolina", 220)

aluno1 = AluEnsinoMedio(2, "Cristiano", 457, 2012)

aluno2 = AlunoGraduacao(3, "Gabriel", 362, "1 semestre")

aluno.imprimir()

print("#"*20)

aluno1.imprimir()

print("#"*20)

aluno2.imprimir()