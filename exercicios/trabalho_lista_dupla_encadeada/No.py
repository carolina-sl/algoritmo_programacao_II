'''

Nó, funciona como um envelope;
tem um espaço pra se colocar o dado
e um espaço pra guardar a posição do nó seguinte com o proximo dado
desse forma conseguimos ligar todos eles
'''


class No:

    def __init__(self, dado):
        self.no = dado
        self.anterior = None
        self.proximo = None
