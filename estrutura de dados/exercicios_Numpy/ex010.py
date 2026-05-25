import numpy as np

"""
🔹 Questão 10
Um sistema de distribuição de água em Maricá pode ser modelado por um sistema de equações lineares. Utilize conceitos de álgebra linear para determinar os valores das variáveis envolvidas, representando a solução do sistema.
"""

A = np.array([
    [3, 1, 2],   
    [1, 4, 0],   
    [2, 0, 5]    
])

B = np.array([10, 15, 20])

try:
    x = np.linalg.solve(A, B)
    
    print("Matriz de Coeficientes (Rede de Água):")
    print(A)
    print("\nVetor de Resultados (Entradas):")
    print(B)
    print("\nSolução do Sistema (Valores das variáveis x1, x2, x3):")
    for i, valor in enumerate(x):
        print(f"Fluxo na Tubulação {i+1}: {valor:.2f} L/s")

except np.linalg.LinAlgError:
    print("Erro: O sistema não pode ser resolvido pois a matriz é singular.")