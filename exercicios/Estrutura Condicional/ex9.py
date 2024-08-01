import datetime
while True:
    try:
        tempo_agora = datetime.datetime.now()
        semana = tempo_agora.strftime('%A')
        mes = tempo_agora.strftime('%B')
        print("")
        print("bem vindo a biblioteca datetime")
        escolha = int(input("Digite (1) para exibir dia,mês e ano, (2) para horas e (3) para os dias da semana: "))

        if escolha == 1:
            if "Januery" == mes:
                traducao = "Janeiro"

            elif "Fabruary" == mes:
                traducao = "Fevereiro"

            elif "March" == mes:
                traducao = "Março"

            elif "April" == mes:
                traducao = "Abril"

            elif "May" == mes:
                traducao = "Maio"

            elif "June" == mes:
                traducao = "Junho"

            elif "July" == mes:
                traducao = "Julho"

            elif "August" == mes:
                traducao = "Agosto"

            elif "September" == mes:
                traducao = "Setembro"

            elif "Octuber" == mes:
                traducao = "Outubro"

            elif "November" == mes:
                traducao = "Novembro"

            elif "Dezember" == mes:
                traducao = "Dezembro"
            print(f"o dia {tempo_agora.day} do mes de {traducao} de {tempo_agora.year}")
            break

        elif escolha == 2:
            if  tempo_agora.hour >= 5 and tempo_agora.hour <= 12:
                print("bom dia")

            elif tempo_agora.hour >= 12 and tempo_agora.hour <= 18:
                print("boa tarde")

            elif tempo_agora.hour >= 18 and tempo_agora.hour <= 24:
                print("boa noite")

            elif tempo_agora.hour >= 24 and tempo_agora.hour <= 5:
                print("boa madrugada")

            print(f"a hora é {tempo_agora.hour}:{tempo_agora.minute} e {tempo_agora.second} segundos")
            break

        elif escolha == 3:
                if "Monday" == semana:
                    traducao = "Segunda"

                elif "Tuesday" == semana:
                    traducao = "Terça"

                elif "Wednesday" == semana:
                    traducao = "Quarta"

                elif "Thursday" == semana:
                    traducao = "Quinta"

                elif "Friday" == semana:
                    traducao = "Sexta"

                elif "Saturday" == semana:
                    traducao = "Sabado"

                elif "Sunday" == semana:
                    traducao = "Domingo"

                print(f"o dia da semana hoje é {traducao} . ")
                break

        else:
            print("informaçao invalida")

    except ValueError:
        print("informaçao invalida")


