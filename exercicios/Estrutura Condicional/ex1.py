print("digite um numero e veja se ele é positivo ou negativo")
print("")
while True:
    try:
        numero = int(input("digite um numero: "))
        if numero > 0:
            print("este numero é positivo")

        else:
            if numero < 0:
                print("este numero é negativo")
        break

    except ValueError:
        print("Erro,digite somente numeros")
