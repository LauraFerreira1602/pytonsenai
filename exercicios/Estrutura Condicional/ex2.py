print("digite duas notas e veja se o aluvo foi aprovado ou reprovado")
print("")
while True:
    try:
        nota1 = float(input("Digite a primeira nota: "))

        if nota1 >= 0 and nota1 <= 100:
            break
        else:
            print("digite uma nota valida entre 0 e 100")

    except ValueError:
        print("digite apenas numeros")

while True:
    try:
        nota2 = float(input("Digite a segunda nota: "))

        if nota2 >= 0 and nota2 <= 100:
            break
        else:
            print("digite uma nota valida entre 0 e 100")

    except ValueError:
        print("digite apenas numeros")

while True:
        media = (nota1 + nota2)/2
        if media >= 70:
            print("O aluno esta aprovado")
            break

        elif media <= 70:
            print("O aluno esta reprovado")
            break

