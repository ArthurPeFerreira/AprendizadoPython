"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

# Atribuindo valores do tipo float para as variáveis numero_1 e numero_2
numero_1 = 0.1
numero_2 = 0.7

# Somando os dois números e armazenando o resultado em numero_3
numero_3 = numero_1 + numero_2

# Imprimindo o valor de numero_3, que devido à representação de ponto flutuante,
# pode não ser exatamente 0.8 por causa de imprecisões inerentes a floats
print(numero_3)  # Saída pode ser algo como 0.7999999999999999

# Imprimindo numero_3 formatado com duas casas decimais, 
# o que visualmente parece 0.80, mas internamente ainda mantém a imprecisão do float
print(f'{numero_3:.2f}')  # Saída: 0.80

# Usando a função round() para arredondar numero_3 para duas casas decimais
# O resultado é mais próximo do valor esperado, mas ainda há imprecisão interna
print(round(numero_3, 2))  # Saída: 0.8

# Agora, usando a classe Decimal do módulo decimal para trabalhar com valores decimais de alta precisão
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')

# Somando os dois números decimais, o resultado será exato
numero_3 = numero_1 + numero_2

# Imprimindo numero_3, que será exatamente 0.8, sem imprecisões de ponto flutuante
print(numero_3)  # Saída: 0.8