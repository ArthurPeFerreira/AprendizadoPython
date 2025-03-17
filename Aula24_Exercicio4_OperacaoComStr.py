# Inicializando as variáveis nome e idade como strings vazias
nome = ""
idade = ""

# Solicitando ao usuário que insira seu nome e idade
nome = input("Digite seu Nome: ")
idade = input("Digite sua Idade: ")

# Calculando o comprimento do nome invertido para uso no fatiamento
comprimento_nome_invertido = (len(nome) + 1) * -1  # Inverte a string de maneira correta
comprimento_nome = len(nome) - 1  # Índice da última letra do nome

# Verificando se ambos os campos (nome e idade) não estão vazios
if nome and idade:  # Verifica se ambas as variáveis contêm valores (não vazias)
    print(f"Seu nome é {nome}")
    
    # Imprimindo o nome invertido usando fatiamento
    print(f"Seu nome invertido é {nome[-1:comprimento_nome_invertido:-1]}")
    
    # Verificando se o nome contém espaços
    if " " in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    
    # Imprimindo o número de letras no nome
    print(f"Seu nome tem {len(nome)} letras")
    
    # Imprimindo a primeira letra do nome
    print(f"A primeira letra do seu nome é {nome[0]}")
    
    # Imprimindo a última letra do nome
    print(f"A última letra do seu nome é {nome[comprimento_nome]}")
else:
    print("Desculpe, você deixou campos vazios")
