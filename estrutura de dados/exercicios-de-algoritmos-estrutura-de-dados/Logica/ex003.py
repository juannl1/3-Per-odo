"""
Escolha de Plano de Saúde: Desenvolva um programa que, baseado na idade
e no estado de saúde do usuário (bom, médio, ruim), determine se ele é
elegível para o plano de saúde premium (requer menos de 40 anos e boa
saúde).
"""

from random import choice



idade = int(input("Digite a idade do paciente: "))
estado_fisico = ["Boa", "Média", "Ruim"]

estado_fisico_sorteado = choice(estado_fisico)

if estado_fisico_sorteado == 'Boa' and idade >= 40:
    print(f"Saúde: {estado_fisico_sorteado}")
    print("Você está elegível para receber nosso plano Premium")

else:
    
    print(f"Saúde: {estado_fisico_sorteado}")
    print("Você está elegível para receber nosso plano Basic")



