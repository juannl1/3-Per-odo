"""
Escolha de Plano de Saúde: Desenvolva um programa que, baseado na idade
e no estado de saúde do usuário (bom, médio, ruim), determine se ele é
elegível para o plano de saúde premium (requer menos de 40 anos e boa
saúde).
"""

from random import choice



idade = int(input("Digite a idade do paciente: "))
estado = ["Bom", "Médio", "Ruim"]

estado_fisico_sorteado = choice(estado)



