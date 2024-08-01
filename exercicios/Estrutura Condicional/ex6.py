print("digite um tres numeros inteiros e mostre o maior deles")
print("")
while True:
    try:
        num1 = int(input("digite o primeiro numero: "))
        num2 = int(input("digite o segundo numero: "))
        num3 = int(input("digite o terceiro numero: "))

        if num1 > num2 and num1 > num3:
            print("o {num1} é o maior deles")
            break

        elif num2 > num1 and num2 > num3:
            print(f"o {num2} é o maior deles")
            break

        else:
            print(f"o {num3} é o maior deles")
            break

    except ValueError:
        print(f"digite apenas numeros")
        break



