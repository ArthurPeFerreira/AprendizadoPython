"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # A função 'soma' é definida com três parâmetros: x, y, e z.
    # Esses parâmetros são as entradas que a função vai usar para realizar sua tarefa.
    
    # Aqui, estamos imprimindo os valores dos parâmetros x, y, e z,
    # e também o resultado da soma desses três valores.
    # O 'f' antes da string permite a formatação, onde {x=} mostra tanto o nome do parâmetro quanto o valor.
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)
    
# Chamando a função 'soma' e passando os valores 1, 2, e 3 para os parâmetros x, y, e z, respectivamente.
soma(1, 2, 3)

# Chamando a função 'soma' novamente, mas agora usando a atribuição dos parâmetros por nome.
# Aqui, x recebe 1, y recebe 2, e z recebe 5.
soma(1, y=2, z=5)

# O print final demonstra o uso de um argumento especial, 'sep', que define o separador entre os valores.
# Nesse caso, os números 1, 2 e 3 serão impressos separados por um hífen '-'.
print(1, 2, 3, sep='-')
