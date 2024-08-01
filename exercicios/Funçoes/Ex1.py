import datetime

def solicite_nome():
    nome_do_usuario = input("Digite seu nome: ")
    return nome_do_usuario

def definindo_saudacao(hora):
    if hora < 0 and hora > 5:
        saudacao = "Boa madrugada "

    elif hora > 5 and hora < 12:
        saudacao = "Bom dia "

    elif hora > 12 and hora < 19:
        saudacao = "Boa tarde "

    else:
        saudacao = "Boa noite "

    return saudacao

def exibir_mensagem(nome, saudacao):
    print(saudacao + nome)

hora = datetime.datetime.now().hour

exibir_mensagem(solicite_nome(), definindo_saudacao(datetime.datetime.now().hour))

