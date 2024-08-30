"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
# Inicializando uma lista vazia que será usada para armazenar os itens de compras
lista_compras = []

# Iniciando um loop infinito que permite ao usuário interagir com o programa até que ele escolha sair
while True:
    # Exibindo o menu de opções para o usuário
    print("Selecione uma opção")
    # Capturando a opção escolhida pelo usuário
    opcao = input("[i]nserir [a]pagar [l]istar [s]air: ")

    # Se o usuário escolher 'i', ele deseja inserir um item na lista de compras
    if opcao == "i":
        # Capturando o nome do item que o usuário deseja inserir e adicionando-o à lista de compras
        lista_compras.append(input("Qual o nome do item que você deseja inserir? "))

    # Se o usuário escolher 'a', ele deseja apagar um item da lista de compras
    elif opcao == "a":
        try:
            # Solicitando ao usuário o índice do item que ele deseja remover
            posicao_item_remover = int(input("Qual o índice do item que você deseja apagar: "))
            # Capturando o item na posição especificada
            item_remover = lista_compras[posicao_item_remover]
            # Removendo o item da lista de compras
            lista_compras.remove(item_remover)
        except:
            # Se houver um erro (por exemplo, o índice não existir), exibe uma mensagem de erro
            print("Não foi possível apagar esse índice.")

    # Se o usuário escolher 'l', ele deseja listar todos os itens na lista de compras
    elif opcao == "l":
        # Verificando se a lista de compras contém algum item
        if len(lista_compras) > 0:
            # Iterando sobre a lista de compras e imprimindo o índice e o nome de cada item
            for indice, nome in enumerate(lista_compras):
                print(indice, nome)
        else:
            # Se a lista estiver vazia, informa ao usuário que não há itens na lista
            print("Não há itens na lista.")

    # Se o usuário escolher 's', o loop é interrompido e o programa termina
    elif opcao == "s":
        break

    # Se o usuário digitar qualquer outra coisa, exibe uma mensagem de opção inválida
    else:
        print("Opção Inválida!")