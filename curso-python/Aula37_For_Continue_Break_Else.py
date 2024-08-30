for i in range(10):  # Loop principal que vai de 0 a 9
    if i == 2:
        print('i é 2, pulando...')
        continue  # Pula o restante do código e vai para a próxima iteração do loop

    if i == 8:
        print('i é 8, seu else não executará')
        break  # Sai do loop quando i é 8, o bloco else do loop for não será executado

    # Loop aninhado que executa duas vezes para cada valor de i
    for j in range(1, 3):
        print(i, j)  # Imprime os valores de i e j

else:
    print('For completo com sucesso!')  # Este else é executado apenas se o loop for não for interrompido por um break
