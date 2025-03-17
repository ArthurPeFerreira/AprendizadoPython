# Unicamente em Python existe a opção while\else
numero1 = 0
numero2 = 0

# Primeiro exemplo: while/else sem break
while numero1 < 3:  # O loop continua enquanto numero1 for menor que 3
    print(numero1)
    numero1 += 1  # Incrementa numero1 em 1 a cada iteração
else:
    # Este bloco 'else' será executado quando a condição do while se tornar falsa
    print("Saiu do While")

# Segundo exemplo: while/else com break
while numero2 < 3:  # O loop continua enquanto numero2 for menor que 3
    print(numero2)
    numero2 += 1  # Incrementa numero2 em 1 a cada iteração
    if numero2 == 2:
        break  # O loop é interrompido quando numero2 for igual a 2
else:
    # Este bloco 'else' NÃO será executado porque o loop foi interrompido com break
    print("Saiu do While")
