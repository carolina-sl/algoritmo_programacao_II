from aula_exercicios_14_14_06.Torre import Torre
from aula_exercicios_14_14_06.Apartamento import Apartamento
from aula_exercicios_14_14_06.Vaga import Vaga


if __name__ == '__main__':

    # while True:
    v1 = Vaga("10")
    v2 = Vaga("20")
    list_vagas_livres = [v1, v2]

    t1 = Torre(1, "Torre 1", 'Meu endereco')

    ap1 = Apartamento(1, "101", None, t1, None)
    ap2 = Apartamento(2, "102", list_vagas_livres.pop(0), t1, None)
    ap3 = Apartamento(3, "103", None, t1, None)
    ap4 = Apartamento(4, "104", list_vagas_livres.pop(0), t1, None)
    ap5 = Apartamento(5, "105", None, t1, None)

    ap1.proximo = ap2
    ap2.proximo = ap3
    ap3.proximo = ap4
    ap4.proximo = ap5

    list_espera_novas_vagas = [ap1, ap3, ap5]

    list_vagas_livres.append(ap2.liberar_vaga())

    ap_vaga_espera = list_espera_novas_vagas.pop(0)

    ap_vaga_espera.vaga = list_vagas_livres.pop(0)

#######################################################

    print(list_vagas_livres)

    for x in list_espera_novas_vagas:
        print(x)
    print("#" * 50)

#######################################################

while True:

    t = Torre(12, "Guanabara", "Assis Brasil")
    t.cadastrar()
    t.imprimir()

    ap1 = Apartamento()
    ap1.cadastrar()
    ap1.imprimir()