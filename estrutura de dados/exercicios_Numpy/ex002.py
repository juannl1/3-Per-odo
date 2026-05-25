import numpy as np

"""🔹 Questão 2
Sensores de temperatura foram instalados em três regiões da cidade de Maricá, registrando dados ao longo de três períodos do dia. Considerando a matriz de dados fornecida, determine o valor total acumulado das medições realizadas.
"""

lista = np.arange(10, 91, 10)
matriz = lista.reshape((3, 3))

valor_total = matriz.sum()

print(matriz)
print(f"\nO valor total acumulado das medições é: {valor_total}")