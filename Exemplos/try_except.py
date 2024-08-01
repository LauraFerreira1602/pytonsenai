while True:
    # O try vai tentar executar esse bloco de codigo
    try:
        idade = int(input('Digite sua idade: '))

        # O if verifica se a idade é valida
        if idade > 0 and idade <= 100:
            print("idade:", idade)
            # O break sai do while
            break
        else:
            print("idade invalida")
    except ValueError:
        # Caso der errado execute aqui
        print("Digite sua idade em numero. Ex: 26")