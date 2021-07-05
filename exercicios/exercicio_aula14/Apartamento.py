from aula_exercicios_14_14_06.Torre import Torre
from aula_exercicios_14_14_06.Vaga import Vaga

list_apartamento = []


class Apartamento:
    id: int
    num_ap: str
    vaga: Vaga
    torre: Torre
    proximo: None

    def __init__(self, id=None, num_ap=None, vaga=None, torre=None, prox_apartamento=None):
        self.id = id
        self.num_ap = num_ap
        self.vaga = vaga
        self.torre = torre
        self.proximo = prox_apartamento

    def imprimir(self):
        print("Apartamento: " + str(self.id), str(self.num_ap), self.vaga, self.torre.nome)

    def __str__(self):
        return "Apartamento: " + str(self.id)

    def cadastrar(self):
        self.id = int(input("digite id do apartamento: "))
        self.num_ap = input("digite o numero do apartamento: ")
        self.num_vaga = Vaga(int(input("digite o numero da vaga: ")))
        self.torre = Torre(str(input("digite a torre: ")))
        ap1 = Apartamento(self.id, self.num_ap, self.num_vaga, self.torre)
        # list_apartamento.append(ap1)

    def liberar_vaga(self):
        vaga_retorno = self.vaga
        self.vaga = None
        return vaga_retorno