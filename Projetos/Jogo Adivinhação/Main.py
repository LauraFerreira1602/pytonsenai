import random #sorteio
print("JOGO DE ADIVINHAÇÃO")
print("")
print("Ola jogador, seja muito bem vindo ao jogo de adivinhação.\nNeste jogo o computador escolhera aleatoriamente um numero\nentre 1 a 100 e voce tera suas chances de chutes até acertar este numero.")
print("")
jogar = "1"
sair = "2"
chute = 0
print("")
while True:
    try:
        escolha = input("Digite 1 se deseja jogar e 2 se deseja sair?: ")
        if escolha == jogar or escolha == sair:
            break
        else:
            print("escolha invalida")

    except ValueError:
        print("Digite sua escolha em numero. Ex: 1-jogar 2-sair")
print("")

if escolha == jogar:
    numero_aleatorio = random.randint(1, 100)

    while escolha != sair:
        while True:
            try:
                chute = int(input("Digite o seu chute: "))
                if chute > 0 or chute < 100:
                    break
                else:
                    print("chute invalido")

            except ValueError:
                print("Digite seu chute em numeros. ex: 1 ou 100")

        if chute > numero_aleatorio:
            print("este numero é maior que o numero escolhido pelo computador")

        elif chute < numero_aleatorio:
            print("este numero é menor que o numero escolhido pelo computador")

        else:
            print("Voce acertou o numero escolhido pelo computador,parabéns!")
            print("")

            while True:
                sair = input("Deseja jogar novamente? (S/N) ")
                if sair == "S" or sair == "N":
                    break
                else:
                    print("saida invalida")

        if sair == "N":
            break
else:
    print("Até a proxima jogador!")