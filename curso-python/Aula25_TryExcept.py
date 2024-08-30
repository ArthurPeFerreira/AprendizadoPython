# Introdução ao try/except
# try -> tenta executar o código dentro do bloco try
# except -> captura e trata erros que ocorrerem durante a execução do código dentro do try

# Solicitando ao usuário que insira um número
numero = input('Vou dobrar o número que você digitar: ')

# Tentativa de conversão do input para float e cálculo do dobro
try:
    # Se a conversão para float for bem-sucedida, imprime o dobro do número
    print(f'O dobro de {float(numero)} é {float(numero) * 2:.2f}')
except:
    # Se ocorrer um erro (como o usuário digitar algo que não seja um número), exibe uma mensagem de erro
    print('Isso não é um número')
