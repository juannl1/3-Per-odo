"""
Elegibilidade para Emprego: Crie um programa que recebe a idade e a
experiência de trabalho (em anos) de um candidato. Se o candidato tiver mais
de 21 anos e pelo menos 2 anos de experiência, imprima "Apto para o
emprego".
"""

idade = int(input("Digite sua idade: "))
exp_trabalho = int(input("Digite seu anos de experiencia completos: "))

if idade >= 21 and exp_trabalho >= 2:
    print("Apto para vaga")
else:
    print("Não está apto para vaga")