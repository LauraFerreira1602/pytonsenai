print("Conversor de Temperatura: digite a temperatura em Celcius e após isso retornaremos o valor convertido para Fahrenheit e Kelvin.")
def solicite_temperatura():
    while True:
        try:
            temperatura_celsios = int(input("Digite a temperatura em celsius: "))
            return temperatura_celsios
        except ValueError:
            print("Digite somente numeros")


def exibir_fahrenheit(temperatura_celsios):
    fahrenheit = temperatura_celsios * 1.8 + 32
    print(f"o valor foi de {fahrenheit}")


def exibir_kelvin(temperatura_celsios):
    kelvin = temperatura_celsios + 273
    print(f"o valor foi de {kelvin}")


temperatura_celsios = solicite_temperatura()

exibir_fahrenheit(temperatura_celsios)
exibir_kelvin(temperatura_celsios)



