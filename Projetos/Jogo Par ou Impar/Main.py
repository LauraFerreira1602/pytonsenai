import random

print("JOGO PAR OU IMPAR")
print("")
print(
    "Ola jogador, seja muito bem vindo ao jogo do par ou impar\n Para começarmos escolha se voce deseja ser par ou impar")
print("\n1-Par\n2-Impar\n0-Sair")

par = 1
impar = 2
sair = 0
numero_aleatorio = random.randint(0, 5)
soma = 0
while True:
    while True:
        try:
            escolha = int(input("Digite sua escolha: "))
            if escolha == 1 or escolha == 2 or escolha == 0:
                break
            else:
                print("escolha invalida")

        except ValueError:
            print("Digite sua escolha em numero. Ex: 1-Par 2-Impar")
    print("")

    while True:
        try:
            numero = int(input("Agora digite um numero de 0 a 5: "))
            if numero > 0 and numero <= 5:
                soma = numero + numero_aleatorio
                print("")
                break
            else:
                print("numero invalido")

        except ValueError:
            print("Digite somente com numeros. Ex: 1 ou 5")

    if soma % 2 == 0:
        if escolha == par:
            print("o numero escolhido pelo computador foi: ", numero_aleatorio)
            print(soma, "é par, voce ganhou")
        else:
            print("o numero escolhido pelo computador foi: ", numero_aleatorio)
            print(soma, "é par, voce perdeu")
    else:
        if escolha == impar:
            print("o numero escolhido pelo computador foi: ", numero_aleatorio)
            print(soma, "é impar, voce ganhou")
        else:
            print("o numero escolhido pelo computador foi: ", numero_aleatorio)
            print(soma, "é impar, voce perdeu")
            print("")

    while True:
        try:
           jogar_novamente = input("voce deseja jogar novamente? (s/n) ")
           if jogar_novamente == "s" or jogar_novamente == "n":
                break
           else:
                print("digite somente s ou n")
        except ValueError:
            print("Digite sua escolha em numero. Ex: s or n")

    if jogar_novamente == "n":
        break
    else:
        numero_aleatorio = random.randint(0, 5)