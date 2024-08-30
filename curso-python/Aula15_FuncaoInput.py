# Pode-se coletar informações do usuário com a função input
# A função input exibe a mensagem 'pergunta' e aguarda a entrada do usuário
pergunta = "Qual seu nome? "
nome = input(pergunta)

# Imprime o nome coletado do usuário
print(f"O seu nome é {nome}")

# A função input retorna um valor em string, portanto, para realizar operações matemáticas,
# é necessário converter essa string para o tipo numérico apropriado (neste caso, int)

# Coletando o primeiro número como string
numero1 = input("Digite o primeiro número: ")

# Coletando o segundo número como string
numero2 = input("Digite o segundo número: ")

# Convertendo as strings para inteiros e somando-os
soma = int(numero1) + int(numero2)

# Imprime o resultado da soma
print(f"A soma é {soma}")
