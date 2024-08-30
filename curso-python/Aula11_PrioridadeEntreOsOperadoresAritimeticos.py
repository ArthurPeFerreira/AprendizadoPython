# Ordem de precedência dos operadores:
# 1. ()   - Parênteses têm a maior prioridade, a expressão dentro deles é avaliada primeiro.
# 2. **   - Exponenciação é avaliada depois dos parênteses.
# 3. * / // % - Multiplicação, Divisão, Divisão Inteira, e Módulo têm a mesma prioridade.
# 4. + -   - Adição e Subtração são avaliadas por último.
# Se os operadores têm a mesma prioridade, a expressão é avaliada da esquerda para a direita.

# Avaliando a expressão passo a passo:
# 1. (3 + 2) -> 5
# 2. 5 ** 3 -> 125
# 3. 125 * 4 -> 500
# 4. 500 - 5 -> 495
conta = (3 + 2) ** 3 * 4 - 5

# Imprime o resultado da expressão avaliada
print(conta)  # Saída: 495
