print("Calculadora IMC: digite seu peso e altura para calcular o imc, e diremos sua classificação")
def imc(peso, altura):
    return peso / (altura * altura)


def peso():
    peso = float(input('Qual o seu peso: '))
    return peso


def altura():
    altura = float(input('Qual a sua altura: '))
    return altura


def classificacao(imc):
   if imc < 18.5:
       print(f"seu imc é {imc}")
       print("Esta pessoa esta abaixo do peso")


   elif imc >= 18.5 and imc < 24.9:
       print(f"seu imc é {imc:.2f}")
       print("Esta pessoa esta com o peso regular")


   elif imc >= 25 and imc < 29.9:
       print(f"seu imc é {imc:.2f}")
       print("Esta pessoa esta sobrepeso")


   elif imc >= 30 and imc < 34.9:
       print(f"seu imc é {imc:.2f}")
       print("Esta pessoa esta obesa grau 1")


   elif imc >= 35 and imc < 39.9:
       print(f"seu imc é {imc:.2f}")
       print("Esta pessoa esta obesa grau 2")

   else:
       print(f"seu imc é {imc:.2f}")
       print("Esta pessoa esta obesa grau 3")


peso = peso()
altura = altura()
imc = imc(peso, altura)
classificacao(imc)