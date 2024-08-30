# ID = identidade na memória que a variável está ocupando
var1 = 'a'
var2 = 'A'

# A função id() retorna o identificador único (endereço de memória) da variável
print(id(var1))  # Exibe o ID (endereço de memória) de 'var1'
print(id(var2))  # Exibe o ID (endereço de memória) de 'var2'

# None = Representa a ausência de valor ou "não valor"
# is e is not = Compara identidade (se é ou não é o mesmo objeto na memória)
# id = Identidade (endereço de memória do objeto)

variavel = None  # Inicializa 'variavel' com None, representando ausência de valor

# Verifica se a variável é None (se está sem valor)
if variavel is None:
    ...  # O "..." é um placeholder que indica que o bloco de código está intencionalmente vazio
elif variavel is not None:
    pass  # O "pass" é uma instrução que não faz nada, usada quando um bloco de código é necessário, mas não deve executar nenhuma ação
