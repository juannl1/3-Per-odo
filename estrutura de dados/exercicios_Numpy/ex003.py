import numpy as np

"""
🔹 Questão 3
Um sistema de monitoramento ambiental coleta dados de poluição do ar em diferentes horários. Cada linha da matriz representa um horário distinto. Calcule a média dos valores de cada linha, de modo a identificar o comportamento médio da poluição ao longo do dia.
"""

lista = np.arange(10, 91, 10)
matriz = lista.reshape((3, 3))

medias_por_horario = matriz.mean(axis=1)

print("Matriz de Poluição (Horário x Sensor):")
print(matriz)

print("\nMédia de poluição por horário:")
for i, media in enumerate(medias_por_horario):
    print(f"Horário {i+1}: {media}")