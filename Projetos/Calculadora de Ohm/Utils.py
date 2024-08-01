
def solicite_tensao_eletrica():
    while True:
        try:
            tensao = float(input("digite a tensão eletrica em volts: "))
            if tensao > 0:
                return tensao
        except ValueError:
            print("Valor invalido, Digite somente numeros")


def solicite_tensao_led():
    while True:
        try:
            tensaoled = float(input("digite a tensao do LED: "))
            if tensaoled > 0:
                return tensaoled
        except ValueError:
            print("Valor invalido, Digite somente numeros")


def solicite_corrente_eletrica():
    while True:
        try:
            corrente = float(input("digite a corrente eletrica em amperes: "))
            if corrente > 0:
                return corrente
        except ValueError:
            print("Valor invalido, Digite somente numeros")


def solicite_resistencia_eletrica():
    while True:
        try:
            resistencia = float(input("digite a resistencia eletrica em ohms: "))
            if resistencia > 0:
                return resistencia
        except ValueError:
            print("Valor invalido, Digite somente numeros")


def menu_calculadora():
    tensao_eletrica = 1
    corrente_eletrica = 2
    resistencia_eletrica = 3
    resistencia_resistor = 4


def escolha():
    while True:
        try:
            escolha1 = int(input("digite sua escolha: "))
            return escolha1
        except ValueError:
            print("Digite somente numeros: ")


def tensao_eletrica(resistencia, corrente):
    return resistencia * corrente


def corrente_eletrica(tensao, resistencia):
    return tensao / resistencia


def resistencia_eletrica(tensao, corrente):
    return tensao / corrente


def resistencia_resistor(tensao, tensaoled, corrente):
    return (tensao - tensaoled) / corrente

# ------------------------------------------------------------------------------------------------------------------


def escolha_final(escolha):
    if escolha == 1:
        resistencia1 = solicite_resistencia_eletrica()
        corrente1 = solicite_corrente_eletrica()
        print(f"a Tensao eletrica é de {tensao_eletrica(resistencia1, corrente1):.2f} volts")

    elif escolha == 2:
        tensao1 = solicite_tensao_eletrica()
        resistencia2 = solicite_resistencia_eletrica()
        print(f"a Corrente eletrica é de {corrente_eletrica(tensao1, resistencia2):.2f} amperes")

    elif escolha == 3:
        tensao = solicite_tensao_led()
        corrente = solicite_corrente_eletrica()
        print(f"a Resistencia eletrica é de {resistencia_eletrica(tensao, corrente):.2f} ohms")

    else:
        tensao = solicite_tensao_led()
        tensaoled = solicite_tensao_led()
        corrente = solicite_corrente_eletrica()
        print(f"a Resistencia do resistor é de {resistencia_resistor(tensao, tensaoled, corrente):.2f}")
