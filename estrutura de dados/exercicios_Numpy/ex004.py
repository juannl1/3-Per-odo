import numpy as np

"""
🔹 Questão 4
Para análise de fluxo de veículos em vias principais de Maricá, um conjunto de dados foi organizado em forma matricial. Para facilitar a interpretação, é necessário reorganizar os dados trocando linhas por colunas. Determine a matriz transposta correspondente.
"""

lista = np.arange(10, 91, 10)
matriz_fluxo = lista.reshape((3, 3))

matriz_transposta = matriz_fluxo.T 

print("Matriz Original (Vias nas Colunas, Horários nas Linhas):")
print(matriz_fluxo)

print("\nMatriz Transposta (Horários nas Colunas, Vias nas Linhas):")
print(matriz_transposta)