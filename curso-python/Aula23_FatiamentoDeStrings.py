# Fatiamento de strings
# Índices positivos:  012345678
# Exemplo de string: "Olá mundo"
# Índices negativos: -987654321

# Fatiamento [inicio(i):fim(f):passo(p)] [i:f:p]
# Obs.: a função len retorna a quantidade de caracteres da string

variavel = "Olá Mundo"

# Acessa o caractere na posição 2 (lembrando que o índice começa em 0)
print(variavel[2])  # Saída: á

# Acessa o caractere na posição -7 (contando de trás para frente)
print(variavel[-7])  # Saída: a

# Pode-se pegar partes da string (fatiamento)
# Pega os caracteres do índice 1 até o índice 2 (o índice final 3 não é incluído)
print(variavel[1:3])  # Saída: lá

# Pega os caracteres do índice 5 até o índice 7 (o índice final 8 não é incluído)
print(variavel[5:8])  # Saída: Mun

# Pega os caracteres do início (índice 0) até o índice 8, com passo 1 (tudo até o final)
print(variavel[0:9:1])  # Saída: Olá Mundo

# Pega os caracteres do início até o índice 8, com passo 2 (pula 1 caractere)
print(variavel[0:9:2])  # Saída: OáMno

# Pega os caracteres do início até o índice 8, com passo 4 (pula 3 caracteres)
print(variavel[0:9:4])  # Saída: Odo

# Pega os caracteres da string de trás para frente, começando do final (-1) até o início (-10)
print(variavel[-1:-10:-1])  # Saída: odnuM álO

# A função len retorna a quantidade de caracteres da string
print(len(variavel))  # Saída: 9

# Pega todos os caracteres do índice 4 até o final da string
print(variavel[4:])  # Saída: Mundo

# Imprime a quantidade de caracteres da substring começando no índice 4 até o final
print(len(variavel[4:]))  # Saída: 5
