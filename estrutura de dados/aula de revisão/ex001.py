"""A prefeitura de Maricá está analisando a quantidade de lixo coletado (em toneladas) em diferentes dias da semana:

lixo = [12, 15, 10, 18, 14]
Desenvolva um programa que:

Calcule o total de lixo coletado

Informe em qual dia ocorreu a maior coleta"""
lixo = [12, 15, 10, 18, 14]

somando_lixo = sum(lixo)
lixo_maximo = max(lixo)
posicao_lista = 0
for itens_lista in lixo:
    if itens_lista == lixo_maximo:
        break
    else:
        pass
    posicao_lista += 1


print(f"No dia {posicao_lista + 1} ele obteve {lixo_maximo} lixos. \nNo total ele obteve {somando_lixo} lixos")