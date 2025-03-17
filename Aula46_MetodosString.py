"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""    
# Definindo uma string 'frase' com espaços extras e uma vírgula separando duas partes da frase
frase = '   Olha só que   , coisa interessante          '

# Usando o método split para dividir a string 'frase' em uma lista de substrings, 
# usando a vírgula como delimitador
lista_frases_cruas = frase.split(',')

# Criando uma lista vazia para armazenar as frases processadas
lista_frases = []

# Iterando sobre cada frase na lista 'lista_frases_cruas'
# Usando lstrip() para remover os espaços à esquerda de cada substring
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].lstrip())
    
# Imprimindo a lista original de frases divididas
print(lista_frases_cruas)

# Imprimindo a lista de frases processadas com os espaços à esquerda removidos
print(lista_frases)    

# Definindo novamente a string 'frase' para reiniciar o processo
frase = '   Olha só que   , coisa interessante          '

# Usando split para dividir a string como antes
lista_frases_cruas = frase.split(',')

# Reinicializando a lista para armazenar as frases com os espaços à direita removidos
lista_frases = []

# Iterando sobre cada frase na lista 'lista_frases_cruas'
# Usando rstrip() para remover os espaços à direita de cada substring
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].rstrip())

# Imprimindo a lista original de frases divididas
print(lista_frases_cruas)

# Imprimindo a lista de frases processadas com os espaços à direita removidos
print(lista_frases)

# Definindo novamente a string 'frase' para reiniciar o processo
frase = '   Olha só que   , coisa interessante          '

# Usando split para dividir a string como antes
lista_frases_cruas = frase.split(',')

# Reinicializando a lista para armazenar as frases com os espaços em ambas as extremidades removidos
lista_frases = []

# Iterando sobre cada frase na lista 'lista_frases_cruas'
# Usando strip() para remover os espaços em ambas as extremidades de cada substring
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# Imprimindo a lista original de frases divididas
print(lista_frases_cruas)

# Imprimindo a lista de frases processadas com os espaços de ambos os lados removidos
print(lista_frases)

# Usando join para unir as frases da lista 'lista_frases' em uma única string
# As frases serão unidas por uma vírgula e um espaço ', '
frases_unidas = ', '.join(lista_frases)

# Imprimindo a string resultante após a união das frases
print(frases_unidas)
 