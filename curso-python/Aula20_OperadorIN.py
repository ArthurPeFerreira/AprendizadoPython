# Operadores in e not in
# Strings são iteráveis, o que significa que você pode acessar seus caracteres usando índices

# Índices positivos:  0 1 2 3 4 5
# Índices negativos: -6-5-4-3-2-1
# Exemplo para a string "arthur"

nome = 'arthur'  # A string 'nome' armazena o valor 'arthur'

# Construindo uma nova string 'nome_contrario' a partir de índices específicos da string 'nome'
# nome[5] -> 'r'
# nome[-2] -> 'u'
# nome[3] -> 'h'
# nome[-4] -> 't'
# nome[1] -> 'r'
# nome[0] -> 'a'
nome_contrario = nome[5] + nome[-2] + nome[3] + nome[-4] + nome[1] + nome[0]

# Imprime o caractere no índice 2 da string 'nome', que é 't'
print(nome[2])  # Saída: t

# Imprime o caractere no índice -4 da string 'nome', que também é 't'
print(nome[-4])  # Saída: t

# Imprime uma linha de separação com 10 caracteres '-'
print("-" * 10)

# Imprime a string original 'nome'
print(nome)  # Saída: arthur

# Imprime a string 'nome_contrario', construída com caracteres específicos de 'nome'
print(nome_contrario)  # Saída: ruhtra

# Imprime uma linha de separação com 10 caracteres '-'
print(10 * '-')

# Verifica se a substring 'ar' está contida na string 'nome'
print('ar' in nome)  # Saída: True (porque 'ar' está em 'arthur')

# Verifica se a substring 'ar' está contida na string 'nome_contrario'
print('ar' in nome_contrario)  # Saída: False (porque 'ar' não está em 'ruhra')

# Imprime uma linha de separação com 10 caracteres '-'
print(10 * '-')

# Verifica se a substring 'ar' NÃO está contida na string 'nome'
print('ar' not in nome)  # Saída: False (porque 'ar' está em 'arthur')

# Verifica se a substring 'ar' NÃO está contida na string 'nome_contrario'
print('ar' not in nome_contrario)  # Saída: True (porque 'ar' não está em 'ruhra')