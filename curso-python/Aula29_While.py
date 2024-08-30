"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira.
Loop infinito -> Quando um código não tem fim.
Break -> Interrompe a execução do while.
Continue -> Pula apenas uma repetição do while e continua com a próxima iteração.
"""

# Inicializa a variável 'condicao' como True, para entrar no loop while
condicao = True

# Inicia um loop que continua enquanto 'condicao' for verdadeira
while condicao:
    # Solicita ao usuário que digite seu nome
    nome = input("Qual seu nome? ")

    # Define 'condicao' como False se o nome digitado for "Arthur"
    condicao = not (nome == "Arthur")

    # Se o usuário digitar 'sair', o loop é interrompido com 'break'
    if nome == 'sair':
        break

# Mensagem exibida quando o loop é encerrado
print("Você Saiu!")

# Inicializa um contador com valor 0
contador = 0

# Inicia um loop que continua enquanto 'contador' for menor ou igual a 100
while contador <= 100:
    print(f"Contador vale: {contador}")
    
    # Incrementa o valor de 'contador' em 1 a cada iteração
    contador = contador + 1

    # Se o contador for igual a 30, exibe uma mensagem e pula para a próxima iteração
    if contador == 30:
        print("Pulou o 30")
        continue  # 'continue' faz o loop pular o restante do código nesta iteração e recomeçar o loop

    # Se o contador for maior que 40, exibe uma mensagem e interrompe o loop
    if contador > 40:
        print("Quebrou no meio")
        break  # 'break' encerra o loop imediatamente

# Mensagem exibida quando o segundo loop é encerrado
print("Você Saiu!")
