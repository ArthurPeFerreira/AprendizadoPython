frase = "O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum."

i = 0
letra_maior_quantidade = ""
letra_maior_quantidade_num = 0

# Converte a frase para minúsculas para evitar diferenciação entre maiúsculas e minúsculas
frase_lower = frase.lower()

while i < len(frase_lower):
    letra_atual = frase_lower[i]
    
    # Conta quantas vezes a letra_atual aparece na frase
    quantidade_letra = frase_lower.count(letra_atual)

    # Se a quantidade de letra_atual for maior que a maior encontrada até agora
    # e a letra não for um espaço
    if quantidade_letra > letra_maior_quantidade_num and letra_atual != " ":
        letra_maior_quantidade = letra_atual
        letra_maior_quantidade_num = quantidade_letra

    i += 1

print(f"A letra de maior quantidade é a letra: '{letra_maior_quantidade}' com um total de: {letra_maior_quantidade_num} ocorrências.")
