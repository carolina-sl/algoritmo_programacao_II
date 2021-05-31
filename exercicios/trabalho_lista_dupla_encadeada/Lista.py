from trabalho_lista_dupla_encadeada.No import No


class ListaDuplamenteEncadeada:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def adicionar(self, valor):
        # Cria o novo No
        novo_no = No(valor)

        # Existem elementos na lista
        if self.inicio:
            # 1 - verificar qual e o ultimo No
            ultimo = self.fim

            # 2 - Atualizar o anterior do ultimo No
            novo_no.anterior = ultimo

            # 3 - Atualizar o proximo No do atual ultimo No
            ultimo.proximo = novo_no

            # 4 - Atualizar o novo ultimo No
            self.fim = novo_no
        else:
            # Não existem elementos na lista
            self.inicio = novo_no
            self.fim = novo_no

        self.tamanho += 1

    def imprimir(self):
        if self.inicio is None:
            print("A lista está vazia")
        else:
            aux = self.inicio
            while aux:
                print(aux.no)
                aux = aux.proximo

            print("Tamanho da lista ", self.tamanho)
            print("--------------------------")
            print('Primeiro item:', self.inicio.no)
            print("--------------------------")
            print('Último item:', self.fim.no)

    def imprimir_inverso(self):
        if self.inicio is None:
            print("A lista está vazia")
        else:
            aux = self.fim
            while aux:
                print(aux.no)
                aux = aux.anterior





