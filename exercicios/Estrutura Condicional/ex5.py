print("digite um numero de 1 a 7 representando um dia na semana")
print("")
dias = 0

while True:
    try:
        dias = int(input("digite um numero de 1 a 7: "))
        if dias >= 1 and dias <= 7:
            break
        else:
            print("este numero é invalido")

    except ValueError:
        print("digite somente numeros de 1 a 7")

if dias == 1:
    print("o numero 1 é igual a segunda-feira")
if dias == 2:
    print("o numero 2 é igual a terça-feira")
if dias == 3:
    print("o numero 3 é igual a quarta-feira")
if dias == 4:
    print("o numero 4 é igual a quinta-feira")
if dias == 5:
    print("o numero 5 é igual a sexta-feira")
if dias == 6:
    print("o numero 6 é igual a sabado-feira")
if dias == 7:
    print("o numero 7 é igual a domingo-feira")

