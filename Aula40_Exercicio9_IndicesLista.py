"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

# Forma 1
lista = ['Maria', 'Helena', 'Luiz']  # Define uma lista de nomes
index = 0  # Inicializa o contador manual com 0

for posicoes in lista:  # Loop que percorre cada item na lista
    print(index, posicoes)  # Exibe o índice atual e o nome correspondente na lista
    index = index + 1  # Incrementa o contador manualmente para o próximo índice


# Forma 2
lista = ['Maria', 'Helena', 'Luiz']  # Define uma lista de nomes
lista.append('João')  # Adiciona o nome 'João' ao final da lista

indices = range(len(lista))  # Cria uma sequência de índices que vai de 0 até o tamanho da lista

for indice in indices:  # Loop que percorre cada índice da lista
    print(indice, lista[indice], type(lista[indice]))  # Exibe o índice, o nome correspondente, e o tipo do item
