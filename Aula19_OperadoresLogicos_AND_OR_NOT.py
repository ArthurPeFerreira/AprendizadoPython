# Operadores lógicos
# São considerados falso: 0, 0.0, '', False
# Também existe o tipo None que é usado para representar um não valor (ausência de valor)

# and (e), or (ou), not (não)

# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será falsa

TesteAND1 = True and True      # Ambos são True, então o resultado é True
TesteAND2 = True and False     # Um dos valores é False, então o resultado é False
TesteAND3 = True and "ABC"     # "ABC" é considerado True, então o resultado é "ABC"
TesteAND4 = True and 1         # 1 é considerado True, então o resultado é 1
TesteAND5 = True and 0         # 0 é considerado False, então o resultado é 0
TesteAND6 = True and ""        # "" (string vazia) é considerado False, então o resultado é ""

print("Exemplos AND:")
print(f"{TesteAND1=}")  # True
print(f"{TesteAND2=}")  # False
print(f"{TesteAND3=}")  # "ABC"
print(f"{TesteAND4=}")  # 1
print(f"{TesteAND5=}")  # 0
print(f"{TesteAND6=}")  # ""

# or - Qualquer condição verdadeira faz com que a expressão inteira seja verdadeira.
# Se qualquer valor for considerado verdadeiro, a expressão inteira será verdadeira.

TesteOR1 = True or True       # Ambos são True, então o resultado é True
TesteOR2 = True or False      # Um dos valores é True, então o resultado é True
TesteOR3 = 1 or True          # 1 é True, então o resultado é 1 (não precisa avaliar o segundo operando)
TesteOR4 = "ABC" or False     # "ABC" é True, então o resultado é "ABC" (não precisa avaliar o segundo operando)
TesteOR5 = False or True      # Um dos valores é True, então o resultado é True
TesteOR6 = True or 1          # O primeiro valor é True, então o resultado é True (não precisa avaliar o segundo operando)

print("\nExemplos OR:")
print(f"{TesteOR1=}")  # True
print(f"{TesteOR2=}")  # True
print(f"{TesteOR3=}")  # 1
print(f"{TesteOR4=}")  # "ABC"
print(f"{TesteOR5=}")  # True
print(f"{TesteOR6=}")  # True

# not - Usado para inverter expressões
# not True = False
# not False = True

TesteNOT1 = True == (not True)     # not True é False, então True == False é False
TesteNOT2 = True == (not False)    # not False é True, então True == True é True
TesteNOT3 = "ABC" == (not False)   # not False é True, então "ABC" == True é False
TesteNOT4 = 1 == (not False)       # not False é True, então 1 == True é True
TesteNOT5 = 1.0 == (not False)     # not False é True, então 1.0 == True é True
TesteNOT6 = 0 == (not True)        # not True é False, então 0 == False é True

print("\nExemplos NOT:")
print(f"{TesteNOT1=}")  # False
print(f"{TesteNOT2=}")  # True
print(f"{TesteNOT3=}")  # False
print(f"{TesteNOT4=}")  # True
print(f"{TesteNOT5=}")  # True
print(f"{TesteNOT6=}")  # True
