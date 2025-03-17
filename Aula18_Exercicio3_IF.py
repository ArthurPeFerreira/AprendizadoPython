# Coletando o primeiro valor do usuário e armazenando como string
primeiro_valor = input("Digite o Primeiro Valor: ")

# Coletando o segundo valor do usuário e armazenando como string
segundo_valor = input("Digite o Segundo Valor: ")

# Inicializando a variável 'string' com uma string vazia
string = ""

# Verifica se o primeiro valor é maior que o segundo
if primeiro_valor > segundo_valor:
    # Se for verdade, formata a string indicando que o primeiro valor é maior
    # O uso de {primeiro_valor=} exibe a expressão e o valor
    string = f"O {primeiro_valor=} é maior que o {segundo_valor=}"
    # Imprime a string formatada
    print(string)

# Verifica se o segundo valor é maior que o primeiro
elif primeiro_valor < segundo_valor:
    # Se for verdade, formata a string indicando que o segundo valor é maior
    string = f"O {segundo_valor=} é maior que o {primeiro_valor=}"
    # Imprime a string formatada
    print(string)
