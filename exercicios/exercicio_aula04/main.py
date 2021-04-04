
from algoritmo_programacao_II.exercicios.exercicio_aula04.Veiculo import Veiculo
from algoritmo_programacao_II.exercicios.exercicio_aula04.Automovel import Automovel
from algoritmo_programacao_II.exercicios.exercicio_aula04.Carro import Carro
from algoritmo_programacao_II.exercicios.exercicio_aula04.Moto import Moto
from algoritmo_programacao_II.exercicios.exercicio_aula04.Bicicleta import Bicicleta


print("*"*50)
print(" CLASSE VEICULO ")
print("*"*50)

v1 = Veiculo("FORD", 4, "KA")
v1.imprimirInformacoes()

##########################################

print("*"*50)
print(" CLASSE AUTOMOVEL ")
print("*"*50)

a1 = Automovel("CHEVROLET", 4, "ONIX", 7, 82.2)
a1.imprimirInformacoes()

##########################################

print("*"*50)
print(" CLASSE CARRO ")
print("*"*50)

c1 = Carro("TOYOTA", 4, "COROLLA", 52, 4, 50)

c1.imprimirInformacoes()
c1.acelerar(100)

##########################################

print("*"*50)
print(" CLASSE MOTO ")
print("*"*50)

m1 = Moto("HONDA", 2, "BIZ", 60.0, True, 150)
m1.imprimirInformacoes()

##########################################

print("*"*50)
print(" CLASSE BICICLETA ")
print("*"*50)

b1 = Bicicleta("Caloi", 2, "elétrica", 6, False)
b1.imprimirInformacoes()

