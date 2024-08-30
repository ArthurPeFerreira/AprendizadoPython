# Coletando a entrada do usuário com a função input
entrada = input('Você quer entrar ou sair? ')

# Verifica se a entrada do usuário é igual a 'entrar'
if entrada == 'entrar':
    # Se a condição for verdadeira, imprime que o usuário entrou no sistema
    print('Você entrou no sistema')

# Verifica se a entrada do usuário é igual a 'sair'
elif entrada == 'sair':
    # Se a condição for verdadeira, imprime que o usuário saiu do sistema
    print('Você saiu do sistema')

# Caso nenhuma das condições anteriores seja atendida
else:
    # Imprime que a entrada foi inválida
    print('Entrada Inválida')
