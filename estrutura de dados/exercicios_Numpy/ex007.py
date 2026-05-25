import numpy as np

"""
🔹 Questão 7
Durante o pré-processamento de dados coletados por sensores urbanos em Maricá, valores abaixo de um determinado limiar devem ser desconsiderados. Substitua todos os valores inferiores ao limite definido por zero, mantendo os demais inalterados.
"""

dados_sensores = np.arange(10, 91, 10).reshape((3, 3))

limiar = 40

dados_limpos = np.where(dados_sensores < limiar, 0, dados_sensores)

print("Dados Originais:")
print(dados_sensores)

print(f"\nDados após pré-processamento (Limiar < {limiar}):")
print(dados_limpos)