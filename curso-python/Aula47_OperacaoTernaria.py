"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
# Avaliando a expressão 10 == 11, que resulta em False
condicao = 10 == 10

# Usando uma expressão condicional (operador ternário) para atribuir um valor à variável 'variavel'
# Se 'condicao' for True, 'variavel' recebe 'Valor'; caso contrário, recebe 'Outro valor'
variavel = 'Valor' if condicao else 'Outro valor'

# Imprimindo o valor de 'variavel', que será 'Outro valor', já que 'condicao' é False
print(variavel)

