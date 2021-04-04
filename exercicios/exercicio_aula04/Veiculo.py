
class Veiculo:
    marca: str
    qtdRodas: int
    modelo: str
    velocidade: int

    def __init__(self, marca, qtdRodas, modelo, velocidade=0):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade

    def imprimirInformacoes(self):
        print("Marca:", self.marca, " \nQuantidade de rodas:", self.qtdRodas, " \nModelo:", self.modelo,
              " \nVelocidade: ", self.velocidade)

    def acelerar(self, valor):
        self.velocidade += valor
        return self.velocidade

    def frear(self, valor):
        self.velocidade -= valor
        return self.velocidade


if __name__ == '__main__':
    v1 = Veiculo("FORD", 4, "KA")

    print("*"*50)
    print(" CLASSE VEICULO ")
    print("*"*50)

    v1.imprimirInformacoes()

    print("#"*50)

    print("Velocidade atual: ", v1.acelerar(50))
    print("Velocidade atual: ", v1.acelerar(100))

    print("#"*50)

    print("Velocidade atual: ", v1.frear(100))

