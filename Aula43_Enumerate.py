"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]

# Criando uma lista com três elementos: 'Maria', 'Helena', 'Luiz'
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# Iterando sobre a lista enumerada, onde enumerate(lista) retorna pares (índice, valor)
# 'item' é uma tupla contendo (índice, nome), que é desempacotada em 'indice' e 'nome'
for item in enumerate(lista):
    indice, nome = item
    # Imprime o índice e o nome correspondente na lista
    print(indice, nome)

# Iterando novamente sobre a lista enumerada, mas dessa vez sem desempacotar a tupla
# Aqui, 'tupla_enumerada' é uma tupla contendo (índice, nome)
for tupla_enumerada in enumerate(lista):
    # Imprimindo uma mensagem para indicar que está dentro do loop da tupla
    print('FOR da tupla:')
    # Iterando sobre cada valor dentro da tupla (primeiro o índice, depois o nome)
    for valor in tupla_enumerada:
        # Imprime cada valor dentro da tupla com um tab para indentação
        print(f'\t{valor}')

# Iterando sobre a lista enumerada e desempacotando diretamente o índice e o nome
for indice, nome in enumerate(lista):
    # Imprime o índice, o nome, e o valor correspondente na lista usando o índice
    print(indice, nome, lista[indice])
