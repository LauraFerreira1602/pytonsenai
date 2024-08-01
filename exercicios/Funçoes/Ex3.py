print("Digite sua escolha, e após isso digite dois numeros para calcularmos")
def soma(numero1, numero2):
    return numero1 + numero2


def subtracao(numero1, numero2):
    return numero1 - numero2


def divisao(numero1, numero2):
    return numero1 / numero2


def multiplicacao(numero1, numero2):
    return numero1 * numero2


def resultado_funcoes(numero1, numero2):

        resultado_soma = soma(numero1, numero2)
        print(f"o resultado da soma foi {resultado_soma}")

        resultado_subtracao = (numero1, numero2)
        print(f"o resultado da subtracao foi {resultado_subtracao}")

        resultado_divisao = (numero1, numero2)
        print(f"o resultado da divisao foi {resultado_divisao}")

        resultado_multiplicacao = (numero1, numero2)
        print(f"o resultado da multiplicacao foi {resultado_multiplicacao}")


def menu_calculadora():
    print("calculadora")
    print("1 - soma")
    print("2 - subitraçao")
    print("3 - multiplicaçao")
    print("4 - divisao")


def escolha_do_usuario():
    escolha = int(input("Digite sua escolha: "))
    return escolha

def numero1():
    numero1 = int(input("Digite o primeiro numero: "))
    return numero1

def numero2():
    numero2 = int(input("Digite o segundo numero: "))
    return numero2
# ---------------------------------------------------------------------------------------------------------
#chamar menu
menu_calculadora()
escolha = escoha_do_usuario()

if escolha == 1:
    resultado_soma = soma(numero1(), numero2())
    print(f"o resultado da soma foi {resultado_soma}")

elif escolha == 2:
    resultado_subtracao = subtracao(numero1(), numero2())
    print(f"o resultado da subtracao foi {resultado_subtracao}")

elif escolha == 3:
    resultado_multiplicacao = multiplicacao(numero1(), numero2())
    print(f"o resultado da multiplicacao foi {resultado_multiplicacao}")

elif escolha == 4:
    resultado_divisao = divisao(numero1(), numero2())
    print(f"o resultado da divisao foi {resultado_divisao}")

