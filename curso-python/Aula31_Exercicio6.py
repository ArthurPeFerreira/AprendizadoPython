# Solicita ao usuário que digite seu nome
nome = input("Digite seu nome: ")

# Calcula o tamanho do nome
tam_nome = len(nome)

# Inicializa um contador para percorrer cada caractere do nome
contador = 0

# Inicializa uma string vazia que será usada para construir o novo nome formatado
string_nome = ""

# Loop para percorrer cada caractere do nome
while (contador < tam_nome):  # Continua enquanto o contador for menor que o tamanho do nome
    if nome[contador] == " ":  # Verifica se o caractere atual é um espaço
        contador += 1  # Se for um espaço, pula para o próximo caractere
        continue  # Usa 'continue' para pular a adição do caractere na string_nome
    
    # Adiciona um '*' antes do caractere e depois o próprio caractere
    string_nome += "*"
    string_nome += nome[contador]
    
    contador += 1  # Incrementa o contador para passar ao próximo caractere
    
    # Se for o último caractere, adiciona um '*' no final
    if contador == tam_nome:
        string_nome += "*"

# Imprime o nome formatado
print(string_nome)
