"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

iniciar_jogo = True
palavra_secreta = "espelho"
chute_letra = ""
palavra_formatada = "*" * len(palavra_secreta)
palavra_formatada_next = ""
comprimento_palavra = range(0,len(palavra_secreta),1)
tentativas = 0

while iniciar_jogo:
    chute_letra = input("Digite uma letra: ")

    if len(chute_letra) > 1:
        print("Digite apenas uma letra.")
        continue

    for i in comprimento_palavra:
        if chute_letra == palavra_secreta[i]:
            palavra_formatada_next += palavra_secreta[i]
        elif palavra_formatada[i] != "*":
            palavra_formatada_next += palavra_formatada[i]
        else:
            palavra_formatada_next += "*"
    
    palavra_formatada = palavra_formatada_next
    palavra_formatada_next = ""
            
    print(f"Palavra formatada: {palavra_formatada}")    
    tentativas += 1

    if palavra_formatada == palavra_secreta:
        iniciar_jogo = False

os.system("cls")
print("VOCÊ GANHOU PARABÉNS!!!")
print(f"A palavra era: {palavra_secreta}")
print(f"Você teve o total de {tentativas} tentativas")