print("digite o ano de nascimento de uma pessoa e veja se ela é maior ou menor de idade")
print("")
while True:
    try:
        ano: int = int(input("digite o ano de nascimento: "))
        idade = 2024 - ano
        print("esta pessoa tem",idade, "anos")
        if idade <= 17 :
            print("esta pessoa é menor de idade")
            break

        elif idade >= 18 and idade <= 120:
            print("esta pessoa é maior de idade")
            break

        else:
            print("esta pessoa faleceu")
            break

    except ValueError:
        print("Digite seu ano de nascimento em numeros. Ex: 2000")
