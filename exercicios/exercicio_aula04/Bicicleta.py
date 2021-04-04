
from algoritmo_programacao_II.exercicios.exercicio_aula04.Veiculo import Veiculo


class Bicicleta(Veiculo):
    numMarchas: int
    bagageiro: bool

    def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro, velocidade=0):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimirInformacoes(self):
        print("Marca:", self.marca, " \nQuantidade de rodas:", self.qtdRodas, " \nModelo:", self.modelo,
              " \nVelocidade: ", self.velocidade, " \nNúmero de marchas: ", self.numMarchas,
              " \nBagageiro: ", self.bagageiro)


if __name__ == '__main__':
    print("*"*50)
    print(" CLASSE BICICLETA ")
    print("*"*50)

    b1 = Bicicleta("Caloi", 2, "elétrica", 6, False, 12)
    b1.imprimirInformacoes()
