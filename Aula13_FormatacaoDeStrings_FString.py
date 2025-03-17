# Armazena o nome completo da pessoa na variável 'nome'
nome = "Arthur Pedro Ferreira"

# Armazena a idade da pessoa na variável 'idade'
idade = 19

# Armazena o peso da pessoa em quilogramas na variável 'peso'
peso = 84.3

# Armazena a altura da pessoa em metros na variável 'altura'
altura = 1.84

# Calcula o Índice de Massa Corporal (IMC) usando a fórmula peso / (altura ** 2)
imc = peso / (altura ** 2)

# Pode-se usar o f-string antes da string, onde assim dá para usar as variáveis dentro das strings entre {}
# O f-string permite incluir expressões dentro de chaves {} diretamente na string e formatá-las
# {altura:.2f} -> formata a altura com 2 casas decimais
# {imc:.3f} -> formata o IMC com 3 casas decimais
linha = f"O {nome} com a idade de {idade} anos, com o peso de {peso} kilos e altura de {altura:.2f} m, tem seu IMC de {imc:.3f}"

# Imprime a linha formatada
print(linha)
