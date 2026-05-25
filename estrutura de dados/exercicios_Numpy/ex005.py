import numpy as np

"""🔹 Questão 5
Em um projeto de modernização da rede elétrica da cidade, duas matrizes representam transformações aplicadas sobre dados de carga elétrica. Realize a multiplicação matricial entre essas duas matrizes, considerando as regras da álgebra linear.
"""

A = np.arange(10, 91, 10).reshape((3, 3))
B = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
])

resultado = A @ B

print("Matriz de Carga (A):")
print(A)

print("\nMatriz de Transformação (B):")
print(B)

print("\nResultado da Multiplicação (A @ B):")
print(resultado)