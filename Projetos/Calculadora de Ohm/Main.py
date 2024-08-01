print("Escolha uma das opçoes para calcular")
print("\n 1-Tensão eletrica\n 2-Corrente eletrica\n 3-Resistencia eletrica\n 4-Resistencia resistor\n 0-sair")

tensao_eletrica = 1
corrente_eletrica = 2
resistencia_eletrica = 3
resistencia_resistor = 4
sair = 0

escolha = int(input("digite sua escolha: "))

while escolha != 0:

    if escolha == tensao_eletrica:
        print("tensao eletrica")
        print("")
        while True:
            try:
                r = float(input("digite a resistencia eletrica em ohms: "))
                if r > 0:
                    break
            except ValueError:
                print("Valor invalido, Digite um numero utilizando o ponto como separador. Ex: 1.0")

            while True:
                i = float(input("digite a corrente eletrica em amperes: "))
                if i > 0:
                    break

        resultado = r * i

        print(f"a Tensao eletrica é de {resultado} volts")

    elif escolha == corrente_eletrica:
        print("corrente eletrica")
        print("")
        while True:
            try:
                v = float(input("digite a tensão eletrica em volts: "))
                if v > 0:
                    break
            except ValueError:
                print("Valor invalido, Digite um numero utilizando o ponto como separador. Ex: 1.0")

        while True:
            r = float(input("digite a resistencia eletrica em ohms: "))
            if r > 0:
                break

        resultado = v / r

        print(f"a Corrente eletrica é de {resultado} amperes")

    elif escolha == resistencia_eletrica:
        print("ressistencia eletrica")
        print("")
        while True:
            try:
                v = float(input("digite a tensão eletrica em volts: "))
                if v > 0:
                    break
            except ValueError:
                print("Valor invalido, Digite um numero utilizando o ponto como separador. Ex: 1.0")

                i = float(input("digite a corrente eletrica em amperes: "))

                resultado = v / i

                print(f"a Resistencia eletrica é de {resultado} ohms")


    elif escolha == resistencia_resistor:
        t = float(input("digite a tensao da fonte: "))
        te = float(input("digite a tensao do LED: "))
        c = float(input("digite a corrente do LED: "))
        resultado1 = t - te
        resultado2 = resultado1 / c
        print(f"a Resistencia resistor é de {resultado2}")

    else:
        print(f"esta opção esta indisponivel")

    print("")
    print("\n 1-Tensão eletrica\n 2-Corrente eletrica\n 3-Resistencia eletrica\n 4-Resistencia resistor\n 0-sair")
    print("")
    escolha = int(input("digite sua escolha: "))
