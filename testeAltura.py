# Apresentação do Teste

def teste_altura():
    print("------------------")
    print("Bem Vindo ao Teste")
    print("------------------")

    nome = str(input("Qual seu nome? "))
    altura = float(input("Qual sua altura? "))

    if altura <= 1.60:
        print(f"{nome}, você está abaixo da média Brasileira.")
    elif altura <= 1.75:
        print(f"{nome}, você está na média Brasileira.")
    elif altura > 1.75:
        print(f"{nome}, você está acima da média Brasileira.")


if __name__ == "__main__":
    teste_altura()
