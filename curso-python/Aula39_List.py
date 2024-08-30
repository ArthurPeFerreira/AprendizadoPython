"""
Listas em Python
Tipo list - Mutável
Tipo list é como se fosse uma array
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#Listas tem indices da mesma forma que strings

#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
print(lista, type(lista))

#Da mesma forma que nos outros tipos de variavel quando temos uma lista vazia temos um valor falso, quando temos outro valor é verdadeira
print(bool([])) 
print(bool(["a","b"]))

"""
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
"""
#        0   1   2   3  
lista = [10, 20, 30, 40]
print(lista)
#Tipo Mutável
lista[2] = 300
print(lista)
#append - Adiciona um item ao final
lista.append(50)
print(lista)
#insert - Adiciona um item no índice escolhido
lista.insert(4, 5)
print(lista[4])
#pop - Remove do final ou do índice escolhido
print(lista,"Removido: ",lista.pop(2))
#del - apaga um índice
del lista[2]
print(lista)
#clear - limpa a lista
lista.clear()
print(lista)
#extend - estende a lista
#+ - concatena listas
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)
