import numpy as np

"""
🔹 Questão 8
Em um estudo de estabilidade de sistemas elétricos, uma matriz representa um sistema linear. Calcule o determinante dessa matriz e analise se o sistema possui solução única.
"""

matriz_sistema = np.arange(10, 91, 10).reshape((3, 3))

det = np.linalg.det(matriz_sistema)

print("Matriz do Sistema:")
print(matriz_sistema)
print(f"\nDeterminante calculado: {det:.2f}")

if det != 0:
    print("Análise: O determinante é diferente de zero. O sistema possui uma solução única (é possível inverter a matriz).")
else:
    print("Análise: O determinante é zero (ou muito próximo de zero). O sistema é singular, o que significa que não possui solução única ou a matriz não é invertível.")