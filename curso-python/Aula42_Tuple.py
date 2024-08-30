"""
Tipo tupla - Uma lista imutável
"""
# Declarando uma tupla chamada 'nomes' com três elementos: 'Maria', 'Helena' e 'Luiz'
nomes = ('Maria', 'Helena', 'Luiz')

print(type(nomes))

# Redefinindo 'nomes' sem usar parênteses, mas ainda assim criando uma tupla
nomes = 'Maria', 'Helena', 'Luiz'

print(type(nomes))

# Convertendo a tupla 'nomes' em uma lista usando a função list()
# Isso permite modificar os elementos posteriormente, pois listas são mutáveis
nomes = list(nomes)

# Convertendo a tupla 'nomes' em uma tupla explicitamente
nomes = tuple(nomes)


