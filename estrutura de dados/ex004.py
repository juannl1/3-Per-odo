"""ocorrencias = {
    "Centro": 25,
    "Inoã": 18,
    "Itaipuaçu": 30,
    "Ponta Negra": 12
}
Crie um programa que:

Calcule o total de ocorrências

Identifique o bairro com menor número de ocorrências

Liste os bairros com mais de 20 ocorrências"""

ocorrencias = {
    "Centro": 25,
    "Inoã": 18,
    "Itaipuaçu": 30,
    "Ponta Negra": 12
}

total_de_ocorrencias = 0
numero_de_ocorrencias = []


for valor in ocorrencias.values():
    if valor:
        numero_de_ocorrencias.append(valor)

        total_de_ocorrencias += 1

menor_indice_de_ocorrencias = min(numero_de_ocorrencias)

for chave, valor in ocorrencias.items():
    if valor == menor_indice_de_ocorrencias:            
        print(f"===================== Menor números de ocorrencias =====================\nCidade: {chave}\nNúmeros de ocorrencias: {valor}")


