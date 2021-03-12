
list_nome_produto = ["chimarrão", "chocolate", "celular", "agua mineral", "banana", "cadeira"]
list_preco_produto = [5.25, 3.10, 1500, 1.50, 2.25, 60]
list_qtd_produto = [1, 2, 10, 4, 8, 2]


def imprimir_lista():
    int_ind = 0
    while int_ind < len(list_nome_produto):
        print("# Produto:", list_nome_produto[int_ind],
              " - Preço:", list_preco_produto[int_ind],
              " - Quantidade: ", list_qtd_produto[int_ind])
        int_ind += 1


def imprimir_produto(produto):

    bln_produto_nao_encontrado = True

    for ind_produto, item_produto in enumerate(list_nome_produto):
        if produto == item_produto:
            print("# Produto encontrado:", list_nome_produto[ind_produto],
                  " - Preço:", list_preco_produto[ind_produto],
                  " - Quantidade: ", list_qtd_produto[ind_produto])

            bln_produto_nao_encontrado = False
            break

    if bln_produto_nao_encontrado:
        print("Produto não encontrado!")


def excluir_produto(produto):
    bln_produto_nao_encontrado = True

    for ind_produto, item_produto in enumerate(list_nome_produto):
        if produto == item_produto:
            print("# Produto excluído:", list_nome_produto[ind_produto],
                  " - Preço:", list_preco_produto[ind_produto],
                  " - Quantidade: ", list_qtd_produto[ind_produto])
            list_nome_produto.pop(ind_produto)
            list_preco_produto.pop(ind_produto)
            list_qtd_produto.pop(ind_produto)

            bln_produto_nao_encontrado = False
            break

    if bln_produto_nao_encontrado:
        print("O produto não pode ser excluido pois não pode ser encontrado!")


def adicionar_produto():
    while True:
        nome = str(input("Digite o nome do produto:"))
        preco = float(input("Digite o preço do produto: "))
        qtd = int(input("Digite a quantidade do produto: "))

        list_nome_produto.append(nome)
        list_preco_produto.append(preco)
        list_qtd_produto.append(qtd)

        imprimir_lista()

        break


if __name__ == '__main__':

    while True:
        escolha = input('''
            1 - Liste os produtos
            2 - Adicione um produto
            3 - Procure um produto
            4 - Exclua um produto
            5 - Saia do programa
            Escolha: ''')

        if escolha == "1":
            imprimir_lista()
        if escolha == "2":
            adicionar_produto()
        if escolha == "3":
            # imprimir_produto("chimarrão")
            imprimir_produto(input('Nome do produto a produrar:'))
        if escolha == "4":
            # excluir_produto("chocolate")
            excluir_produto(input('Nome do produto a excluir:'))
        if escolha == "5":
            print("Saindo...")
            break












