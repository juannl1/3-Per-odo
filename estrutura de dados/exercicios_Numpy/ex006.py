import numpy as np

"""
🔹 Questão 6
Um sistema de monitoramento de pressão em tubulações identifica valores críticos que podem indicar risco de falha. Considerando uma matriz de dados, identifique todos os valores superiores a um limite estabelecido de segurança.
"""

pressao = np.arange(10, 91, 10).reshape((3, 3))

limite = 60

mascara = pressao > limite

valores_criticos = pressao[mascara]

print("Matriz de Pressão:")
print(pressao)

print(f"\nValores acima do limite ({limite}):")
print(valores_criticos)