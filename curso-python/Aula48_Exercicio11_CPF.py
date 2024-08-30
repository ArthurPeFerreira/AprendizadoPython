import re

# Função para validar o primeiro dígito verificador do CPF
def ValidarPrimeiroDigitoVerificador(Lista_cpf):
    # Lista para armazenar os resultados da multiplicação dos dígitos do CPF
    lista_digitos_multiplicacao = []
    
    # Valor inicial da multiplicação, que começa em 10 e vai decrescendo
    inicial_multiplicacao = 10
    
    # Variável para armazenar o somatório dos dígitos multiplicados
    somatorio_digitos = 0
    
    # Iterando sobre os dígitos da lista do CPF
    for indice, digitos in enumerate(Lista_cpf):
        # Multiplicando cada dígito pelo valor correspondente e armazenando na lista
        lista_digitos_multiplicacao.append(digitos * inicial_multiplicacao)
        # Reduzindo o valor da multiplicação para o próximo dígito
        inicial_multiplicacao -= 1
    
    # Somando todos os valores obtidos na multiplicação
    for i in range(0, len(Lista_cpf), 1):
        somatorio_digitos += lista_digitos_multiplicacao[i]
    
    # Calculando o primeiro dígito verificador
    if somatorio_digitos % 11 < 10:
        digito_verificador = 11 - (somatorio_digitos % 11)
    else:
        digito_verificador = 0
    
    # Retornando o primeiro dígito verificador
    return digito_verificador

# Função para validar o segundo dígito verificador do CPF
def ValidarSegundoDigitoVerificador(Lista_cpf):
    # Primeiro, adiciona o primeiro dígito verificador à lista do CPF
    Lista_cpf.append(ValidarPrimeiroDigitoVerificador(Lista_cpf))
    
    # Lista para armazenar os resultados da multiplicação dos dígitos do CPF
    lista_digitos_multiplicacao = []
    
    # Valor inicial da multiplicação, que começa em 11 e vai decrescendo
    inicial_multiplicacao = 11
    
    # Variável para armazenar o somatório dos dígitos multiplicados
    somatorio_digitos = 0
    
    # Iterando sobre os dígitos da lista do CPF
    for indice, digitos in enumerate(Lista_cpf):
        # Multiplicando cada dígito pelo valor correspondente e armazenando na lista
        lista_digitos_multiplicacao.append(digitos * inicial_multiplicacao)
        # Reduzindo o valor da multiplicação para o próximo dígito
        inicial_multiplicacao -= 1
    
    # Somando todos os valores obtidos na multiplicação
    for i in range(0, len(Lista_cpf), 1):
        somatorio_digitos += lista_digitos_multiplicacao[i]
    
    # Calculando o segundo dígito verificador
    if somatorio_digitos % 11 < 10:
        digito_verificador = 11 - (somatorio_digitos % 11)
    else:
        digito_verificador = 0
    
    # Retornando o segundo dígito verificador
    return digito_verificador

# Variável para armazenar o CPF como string
string_cpf = ""
# Lista para armazenar os dígitos do CPF como inteiros
lista_digitos_cpf = []

# Loop para garantir que o usuário insira exatamente 9 dígitos
while True:
    # Solicitando a entrada do CPF
    entrada = input("Digite os 9 Primeiros Digitos do seu CPF: ")
    # Removendo qualquer caractere que não seja numérico da entrada
    string_cpf = re.sub(
        r'[^0-9]',
        '',
        entrada
    )
    
    # Verificando se a entrada tem exatamente 9 dígitos
    if len(string_cpf) < 9 or len(string_cpf) > 9:
        print("CPF Inválido, digite-o corretamente")
    else:
        # Se a entrada for válida, sai do loop
        break

# Convertendo cada caractere da string do CPF em um inteiro e adicionando à lista
for indice, digitos in enumerate(string_cpf):
    lista_digitos_cpf.append(int(digitos))

# Imprimindo o primeiro dígito verificador calculado
print(ValidarPrimeiroDigitoVerificador(lista_digitos_cpf))

# Imprimindo o segundo dígito verificador calculado
print(ValidarSegundoDigitoVerificador(lista_digitos_cpf))