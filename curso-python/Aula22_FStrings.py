# Formatação básica de strings usando f-strings
# s - string
# d - int
# f - float
# .<número de dígitos>f - Define o número de casas decimais em um float
# x ou X - Hexadecimal (minúsculo ou maiúsculo)
# (Caractere)(><^)(quantidade) - Alinhamento e preenchimento
# > - Alinha à direita
# < - Alinha à esquerda
# ^ - Centraliza
# = - Força o número a aparecer antes dos zeros no caso de preenchimento
# Sinal - + ou - para indicar positivo ou negativo
# Exemplo: 0>-100,.1f - Formata um número com alinhamento à direita, preenchendo com zeros, com 1 casa decimal
# Conversion flags - !r !s !a

variavel = "ABCD"
valor = 10

# Imprime a variável 'variavel' sem formatação adicional
print(f"{variavel}")  # Saída: ABCD

# Alinha 'variavel' à direita em um espaço de 10 caracteres
print(f"{variavel: >10}")  # Saída:       ABCD (com 6 espaços à esquerda)

# Alinha 'variavel' à esquerda em um espaço de 10 caracteres
print(f"{variavel: <10}")  # Saída: ABCD      (com 6 espaços à direita)

# Centraliza 'variavel' em um espaço de 10 caracteres, preenchendo com o caractere '$'
print(f"{variavel:$^10}")  # Saída: $$$ABCD$$$ (com 3 '$' à esquerda e 3 '$' à direita)

# Formata um número float com 1 casa decimal, incluindo o sinal de positivo, e separa os milhares por vírgula
print(f"{1323.23213123213:+,.1f}")  # Saída: +1,323.2 (com vírgula como separador de milhar)

# Converte 'valor' em hexadecimal com 8 dígitos, preenchendo com zeros à esquerda
print(f"O Hexadecimal de {valor} é {valor:08X}")  # Saída: O Hexadecimal de 10 é 0000000A
