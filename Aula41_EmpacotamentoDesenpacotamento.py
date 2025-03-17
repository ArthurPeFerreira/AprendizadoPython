"""
Introdução ao empacotamento e desempacotamento
"""
# Lista com três elementos: 'Maria', 'Helena', 'Luiz'
nomes = ['Maria', 'Helena', 'Luiz']

# Desempacotando a lista:
# O primeiro e o segundo elementos ('Maria' e 'Helena') são ignorados usando _
# O terceiro elemento ('Luiz') é atribuído à variável 'nome'
# Como não há mais elementos na lista, 'resto' será uma lista vazia
_, _, nome, *resto = nomes

# Imprime o valor da variável 'nome', que contém 'Luiz'
print(nome)

