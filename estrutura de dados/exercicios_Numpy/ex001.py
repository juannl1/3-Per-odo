import numpy as np

"""
Em um estudo sobre o consumo de energia elétrica em diferentes bairros de Maricá, um engenheiro organizou os dados em forma matricial para facilitar a análise. Construa uma matriz 3x3 contendo valores de 10 a 90, com incremento de 10, organizados linha por linha.
"""

lista = np.arange(10, 91, 10)
matriz = lista.reshape((3, 3))

print(matriz)