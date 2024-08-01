print("digite um numero de 1 a 12 representando um mes do ano")
print("")
while True:
        try:
            mes = int(input("digite um numero de 1 a 12: "))
            if mes >= 1 and mes <= 12:
                break
            else:
                print("este numero é invalido")

        except ValueError:
            print("digite somente numeros de 1 a 12")

if mes == 1:
    print("o mes 1 é janeiro")
if mes == 2:
    print("o mes 2 é fevereiro")
if mes == 3:
    print("o mes 3 é março")
if mes == 4:
    print("o mes 4 é abril")
if mes == 5:
    print("o mes 5 é maio")
if mes == 6:
    print("o mes 6 é junho")
if mes == 7:
    print("o mes 7 é julho")
if mes == 8:
    print("o mes 8 é agosto")
if mes == 9:
    print("o mes 9 é setembro")
if mes == 10:
    print("o mes 10 é outubro")
if mes == 11:
    print("o mes 11 é novembro")
if mes == 12:
    print("o mes 12 é dezembro")