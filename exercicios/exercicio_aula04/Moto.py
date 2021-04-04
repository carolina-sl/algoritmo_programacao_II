
from algoritmo_programacao_II.exercicios.exercicio_aula04.Automovel import Automovel


class Moto(Automovel):
    partidaEletrica: bool

    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, partidaEletrica, velocidade=0):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.partidaEletrica = partidaEletrica

    def imprimirInformacoes(self):
        print("Marca:", self.marca, " \nQuantidade de rodas:", self.qtdRodas, " \nModelo:", self.modelo,
              " \nVelocidade: ", self.velocidade, " \nPotencia do motor: ", self.potenciaDoMotor,
              " \nPartida elétrica: ", self.partidaEletrica)


if __name__ == '__main__':
    print("*"*50)
    print(" CLASSE MOTO ")
    print("*"*50)

    m1 = Moto("HONDA", 2, "BIZ", 60.0, True, 150)
    m1.imprimirInformacoes()
