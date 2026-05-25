import numpy as np

"""
🔹 Questão 9
Para resolver um sistema elétrico equivalente, é necessário obter a matriz inversa associada ao sistema. Determine a matriz inversa, caso ela exista, e interprete sua utilidade no contexto do problema.
"""

matriz = np.arange(10, 91, 10).reshape((3, 3))

det = np.linalg.det(matriz)

print("Matriz Original:")
print(matriz)

if np.isclose(det, 0):
    print(f"\nDeterminante: {det:.2f}")
    print("Resultado: A matriz é SINGULAR (determinante zero), portanto não possui inversa.")
else:
    matriz_inversa = np.linalg.inv(matriz)
    print("\nMatriz Inversa:")
    print(matriz_inversa)