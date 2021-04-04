
from algoritmo_programacao_II.exercicios.exercicio_aula04.Veiculo import Veiculo


class Automovel(Veiculo):
    potenciaDoMotor: float

    def __init__(self, marca, qtdRodas, modelo,potenciaDoMotor, velocidade=0):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.potenciaDoMotor = potenciaDoMotor

    def imprimirInformacoes(self):
        print("Marca:", self.marca, " \nQuantidade de rodas:", self.qtdRodas, " \nModelo:", self.modelo,
              " \nVelocidade: ", self.velocidade, " \nPotencia do motor: ", self.potenciaDoMotor)


if __name__ == '__main__':
    print("*"*50)
    print(" CLASSE AUTOMOVEL ")
    print("*"*50)

    a1 = Automovel("CHEVROLET", 4, "ONIX", 7, 82.2)

    print('########### Automovel')
    a1.imprimirInformacoes()

    print('########### Veículo')
    a1.__class__ = Veiculo
    a1.imprimirInformacoes()
