"""
Operadores de atribuição
=   -> Atribui um valor à variável
+=  -> Soma e atribui o resultado à variável
-=  -> Subtrai e atribui o resultado à variável
*=  -> Multiplica e atribui o resultado à variável
/=  -> Divide e atribui o resultado à variável
//= -> Divide por inteiro e atribui o resultado à variável
**= -> Eleva à potência e atribui o resultado à variável
%=  -> Calcula o resto da divisão e atribui o resultado à variável
"""
numero = 10
string = "A"

# Números
print(numero)  # Imprime o valor inicial de 'numero', que é 10

# Soma o número e atribui o resultado à variável 'numero'
numero += 1
print(numero)  # Imprime 11 (10 + 1)

# Subtrai do número e atribui o resultado à variável 'numero'
numero -= 1
print(numero)  # Imprime 10 (11 - 1)

# Multiplica o número e atribui o resultado à variável 'numero'
numero *= 10
print(numero)  # Imprime 100 (10 * 10)

# Divide o número e atribui o resultado à variável 'numero'
numero /= 2
print(numero)  # Imprime 50.0 (100 / 2)

# Divide o número por inteiro e atribui o resultado à variável 'numero'
numero //= 2
print(numero)  # Imprime 25.0 (50.0 // 2)

# Eleva o número à potência de 10 e atribui o resultado à variável 'numero'
numero **= 10
print(numero)  # Imprime 95367431640625.0 (25.0 ** 10)

# Calcula o resto da divisão do número por 2 e atribui o resultado à variável 'numero'
numero %= 2
print(numero)  # Imprime 1.0 (95367431640625.0 % 2)

# Strings
print(string)  # Imprime o valor inicial de 'string', que é "A"

# Concatena a string com "B" e atribui o resultado à variável 'string'
string += "B"
print(string)  # Imprime "AB"

# Multiplica a string pelo valor 10 e atribui o resultado à variável 'string'
string *= 10
print(string)  # Imprime "ABABABABABABABABABAB"
