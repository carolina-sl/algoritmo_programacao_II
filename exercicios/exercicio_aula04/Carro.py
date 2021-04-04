
from algoritmo_programacao_II.exercicios.exercicio_aula04.Automovel import Automovel


class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, qtdPortas, velocidade=0):
        Automovel.__init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.qtdPortas = qtdPortas

    def imprimirInformacoes(self):
        print("Marca:", self.marca, " \nQuantidade de rodas:", self.qtdRodas, " \nModelo:", self.modelo,
              " \nVelocidade: ", self.velocidade, " \nPotencia do motor: ", self.potenciaDoMotor,
              " \nQuantidade de portas: ", self.qtdPortas)


if __name__ == '__main__':
    print("*"*50)
    print(" CLASSE CARRO ")
    print("*"*50)

    c1 = Carro("TOYOTA", 4, "COROLLA", 52, 4, 50)

    c1.imprimirInformacoes()
    c1.acelerar(100)
