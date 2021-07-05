

list_torre = []


class Torre:
    id: int
    nome: str
    endereco: str

    def __init__(self, id=None, nome=None, endereco=None):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        return '> id:' + str(self.id) + '.Nome da Torre: ' + str(
            self.nome) + ' - Endereço: ' + str(self.endereco)

    def cadastrar(self):
        self.id = input("digite o id da torre: ")
        self.nome = input("digite o nome da torre: ")
        self.endereco = input("digite o endereço da torre: ")
        t1 = Torre(self.id, self.nome, self.endereco)
        list_torre.append(t1)

    def imprimir(self):
        for dado in list_torre:
            print("Id:", dado.id, " Nome:", dado.nome, " Endereço:", dado.endereco)


'''while True:
    t = Torre()
    t.cadastrar()
    t.imprimir()'''