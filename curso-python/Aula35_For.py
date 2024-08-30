"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

#Como o For funciona da forma indireta:

texto = 'Arthur'  # iterável

#Usa-se  o metodo __iter__ para puxar o objeto iterador e pode ser feito das seguintes formas:
iteratador = texto.__iter__()  # iterator
iteratador = iter(texto)  # iterator

while True:
    try:
        #Usa-se  o metodo __next__ para puxar o proximo valor do iterador e pode ser feito das seguintes formas:
        letra = next(iteratador)
#        letra = iteratador.__next__()
        print(letra)
    except StopIteration:         
        break

print("\n")

#Portanto temos a mesma coisa quando usamos o for:

for letra in texto:
    print(letra)

#Onde letra é uma variavel criada internamente no bloco for para pegar os valores do objeto iteravel