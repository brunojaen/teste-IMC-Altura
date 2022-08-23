# Apresentação do Teste

def teste_imc():
    print("----------------------")
    print("Bem Vindo ao Teste IMC")
    print("----------------------")

    nome = str(input("Qual seu nome? "))
    peso = float(input("Qual seu peso? "))
    altura = float(input("Qual sua altura? "))
    imc = peso / (altura * altura)

    if imc < 18.5:
        print(f"{nome}, você está abaixo do peso.")
    elif imc <= 24.9:
        print(f"{nome}, você está com o peso normal.")
    elif imc <= 29.9:
        print(f"{nome}, você está acima do peso.")
    else:
        print(f"{nome}, você está com obesidade")


if __name__ == "__main__":
    teste_imc()
