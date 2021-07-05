class Vaga:
    numero: str

    def __init__(self, numero):
        self.numero = numero

    def __str__(self):
        return 'Número: ' + str(self.numero)