from datetime import datetime

def menu_calculadora():
    print("calculadora")
    print("1 - soma")
    print("2 - subitraçao")
    print("3 - multiplicaçao")
    print("4 - divisao")


def return_ola_nome(nome):
    print(f"ola {nome}")


def ola_nome(nome):
    print(f"ola {nome}")


def calcular_idade(data_de_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - data_de_nascimento
    return idade


def exibir_idade(data_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - data_nascimento
    print("a sua idade é",idade)


def solicita_ano_nascimento():
    while True:
        try:
            ano_de_nascimento = int(input("Digite o ano de nascimento: "))
            if ano_de_nascimento > datetime.now().year:
                print("Digite um valor ano valido")
            else:
                return ano_de_nascimento
        except ValueError:
            print("Digite um valor inteiro. Ex.: 1997")


# Exibe o menu da calculadora
menu_calculadora()


# Exibe o menu da calculadora
ola_nome("Laura")


# Exiba o return
print(return_ola_nome("Laura"))

ola_nome("Laura")



print(calcular_idade(data_de_nascimento = 1997))

exibir_idade(1997)

ano_nascimento = solicita_ano_nascimento()

exibir_idade(ano_nascimento)

