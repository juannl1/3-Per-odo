"""Durante uma ação de vacinação em Maricá, foram registrados os atendimentos realizados em diferentes postos:

vacinacao = [200, 150, 300, 250, 180]
Crie um programa que:

Conte quantos postos atenderam mais de 200 pessoas

Exiba os valores desses atendimentos"""

vacinacao = [200, 150, 300, 250, 180]

contando = 1

for qtd_pessoas in vacinacao:
    if qtd_pessoas > 200:
        print(f"Posto {contando}: {qtd_pessoas} pessoas")
        contando += 1



