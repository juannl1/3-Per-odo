"""Um levantamento foi feito em Maricá sobre o tempo médio de deslocamento (em minutos) entre bairros:

bairros = ("Centro", "Inoã", "Itaipuaçu", "Ponta Negra")
tempos = (20, 35, 40, 25)
Desenvolva um programa que:

Identifique o bairro com maior tempo de deslocamento

Mostre o valor correspondente"""

bairros = ("Centro", "Inoã", "Itaipuaçu", "Ponta Negra")
tempos = (20, 35, 40, 25)

tempo_max = max(tempos)

posicao_lista_tempo = 1

for tempo in tempos:
    if tempo == tempo_max:
        posicao_lista_tempo += 1

print("===================== Maior tempo de deslocamento =====================")
print(f"Bairro: {bairros[posicao_lista_tempo]} \nTempo de deslocamento: {tempos[posicao_lista_tempo]}")