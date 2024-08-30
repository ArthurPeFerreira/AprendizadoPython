"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input("Digite um número para saber se este é par ou ímpar: ")

# Verifica se o valor digitado é um número inteiro usando isdigit()
if numero.isdigit():
    numero_inteiro = int(numero)
    if numero_inteiro % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
else:
    print("Por favor, digite um número inteiro válido.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input("Digite a hora (0-23): ")

# Verifica se o valor digitado é um número inteiro e se está dentro do intervalo válido
if hora.isdigit():
    hora_int = int(hora)
    if 0 <= hora_int <= 11:
        print("Bom Dia")
    elif 12 <= hora_int <= 17:
        print("Boa Tarde")
    elif 18 <= hora_int <= 23:
        print("Boa Noite")
    else:
        print("Por favor, digite uma hora válida entre 0 e 23.")
else:
    print("Por favor, digite um número inteiro válido.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite seu nome: ")

# Verifica o comprimento do nome e exibe a mensagem apropriada
if len(nome) <= 4:
    print("Seu nome é curto.")
elif 5 <= len(nome) <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")
