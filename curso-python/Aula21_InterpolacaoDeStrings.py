# Interpolação de Strings
# %s - Substitui por uma string
# %d ou %i - Substitui por um valor inteiro (decimal)
# %f - Substitui por um valor de ponto flutuante (float)
# %x ou %X - Substitui por um valor em formato hexadecimal (minúsculo ou maiúsculo, respectivamente)

Nome = "Arthur"  # Armazena a string "Arthur" na variável Nome
Idade = 19       # Armazena o valor inteiro 19 na variável Idade
Altura = 1.83232 # Armazena o valor de ponto flutuante 1.83232 na variável Altura

# Usando a interpolação de strings com o operador %
# %s é substituído por Nome (string)
# %d é substituído por Idade (inteiro)
# %04X converte Idade para hexadecimal com 4 dígitos e letras maiúsculas
# %.2f formata Altura com 2 casas decimais
Printar = "%s, tem %d anos, sendo %04X em Hexadecimal e Mede %.2f metros" % (Nome, Idade, Idade, Altura)

# Imprime a string interpolada com os valores substituídos
print(Printar)
