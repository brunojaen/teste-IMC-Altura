import testeIMC
import testeAltura


def escolher_teste():
    print("------------------------------------")
    print("Escolha qual teste gostaria de fazer")
    print("------------------------------------")

    print("(1) Teste de IMC (2) Teste de Altura")

    teste = int(input("Qual Teste? "))

    if (teste == 1):
        print("Teste de IMC")
        testeIMC.teste_imc()
    elif (teste == 2):
        print("Teste de Altura")
        testeAltura.teste_altura()


if __name__ == "__main__":
    escolher_teste()
