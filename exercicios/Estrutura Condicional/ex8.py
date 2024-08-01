print("digite o valor da sua conta bruta e calcule para ver o desconto que ira receber")
print("")
while True:
    try:
        valor = int(input("Digite o valor de sua renda anual bruta: "))
        break
    except ValueError:
        print("digite em numeros o seu valor.")

if valor <= 56072.00:
    print("Não ha desconto")

elif valor >= 56072.01 and valor <= 238532.00:
     desconto1 = (7.50 / 100) * valor
     print(f"o seu desconto será de {desconto1} reais")

elif valor >= 238532.01 and valor <= 522400.00:
    desconto2 = (15 / 100) * valor
    print(f"o seu desconto será de {desconto2} reais")

elif valor >= 522400.01 and valor <= 987600.00:
    desconto3 = (22.50 / 100) * valor
    print(f"o seu desconto será de {desconto3} reais")

elif valor >= 987600.00:
    desconto4 = (27.50 / 100) * valor
    print(f"o seu desconto será de {desconto4} reais")

