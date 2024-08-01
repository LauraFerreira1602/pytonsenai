print("digite dois numeros e veja qual é maior e qual é menor")
print("")
while True:
    try:
        numero1 = int(input("digite o primeiro numero: "))
        numero2 = int(input("digite o segundo numero: "))

        if numero1 > numero2:
            print(f"o {numero1} é maior do que o {numero2}")
            break

        elif numero2 > numero1:
            print(f"o {numero2} é maior do que o {numero1}")
            break

        else:
            print(f"o {numero1} < {numero2}")
            break

    except ValueError:
        print("digite apenas numeros. Ex: 11 ou 12")