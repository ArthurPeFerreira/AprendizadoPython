a = "AAAA"
b = "BBBB"
c = 1.3252

# Podemos usar o método .format para formatar strings
# Aqui, as variáveis 'a', 'b', e 'c' são inseridas na string nas posições correspondentes
# c={:.2f} formata o valor de 'c' para ter 2 casas decimais
string1 = "a={} b={} c={:.2f}"
formatado1 = string1.format(a, b, c)

# Imprime a string formatada, onde 'a', 'b', e 'c' são substituídos pelos valores de 'a', 'b', e 'c'
print(formatado1)

# Para pegar o parâmetro específico, usa-se a sua ordem, começando de 0
# {1} refere-se ao segundo argumento de .format(), que é 'b'
# {2:.2f} refere-se ao terceiro argumento, que é 'c', formatado com 2 casas decimais
# {0} refere-se ao primeiro argumento, que é 'a'
string2 = "b={1} c={2:.2f} a={0}"
formatado2 = string2.format(a, b, c)

# Imprime a string formatada com os parâmetros na ordem especificada
print(formatado2)

# Pode-se nomear os parâmetros também
# Aqui, nome1, nome2, e nome3 são os nomes dados aos parâmetros, que são associados às variáveis 'a', 'b', e 'c'
string3 = "b={nome2} c={nome3:.2f} a={nome1}"
formatado3 = string3.format(nome1=a, nome2=b, nome3=c)

# Imprime a string formatada com os parâmetros nomeados
print(formatado3)
