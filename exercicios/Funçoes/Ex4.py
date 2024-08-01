print("Digite três numeros para determinar os lados do triangulo e veja se ele é equilátero, isósceles ou escaleno.")
def primeiro_numero():
    while True:
        try:
            lado1 = int(input("Digite o primeiro numero: "))
            return lado1
        except ValueError:
            print("digite somente numeros")


def segundo_numero():
    while True:
        try:
            lado2 = int(input("Digite o segundo numero: "))
            return lado2
        except ValueError:
            print("digite somente numeros")


def terceiro_numero():
    while True:
        try:
            numero3 = int(input("Digite o terceiro numero: "))
            return numero3
        except ValueError:
            print("digite somente numeros")


def identificacao_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
        print("Todos os lados possuem medidas iguais este triangulo é equilatero")

    elif lado1 == lado2 and lado1 != lado3 and lado1 != lado3 or lado1 == lado3 and lado1 != lado2 or lado2 == lado3 and lado2 != lado1:
        print("So ha dois lados com medidas iguais neste triangulo, este triangulo é isoceles")

    else:
        print("Todos os lados possuem medidas diferentes este triangulo é escaleno")


numero1 = primeiro_numero()
numero2 = segundo_numero()
numero3 = terceiro_numero()
identificacao_triangulo(numero1, numero2, numero3)