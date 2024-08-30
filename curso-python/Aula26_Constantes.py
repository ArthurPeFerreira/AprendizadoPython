# É convencionado:
# CONSTANTE = "Variáveis" que não vão mudar
# variaveis = "Variáveis" que podem mudar
# OBS: É apenas uma convenção. Se o valor de uma constante for alterado no código, seu valor será realmente alterado.

# Definindo uma constante (por convenção, em letras maiúsculas)
CONSTANTE1 = 10

# Definindo uma variável que poderá mudar
variavel1 = 1

# Calculando a multiplicação da constante pelo valor da variável
multiplicacao = CONSTANTE1 * variavel1

# Imprimindo o resultado da multiplicação
print(f'O valor da variável1 é igual a {variavel1}, que multiplicado pela constante de valor {CONSTANTE1} é {multiplicacao}')

# Alterando o valor da variável
variavel1 = 2

# Recalculando a multiplicação com o novo valor da variável
multiplicacao = CONSTANTE1 * variavel1

# Imprimindo o novo resultado da multiplicação
print(f'O valor da variável1 é igual a {variavel1}, que multiplicado pela constante de valor {CONSTANTE1} é {multiplicacao}')
