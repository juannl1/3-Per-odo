"""
 Faixas Etárias: Implemente um programa que recebe uma idade do usuário
e classifica a pessoa como "Criança" (até 12 anos), "Adolescente" (13 a 17
anos), "Adulto" (18 a 64 anos) ou "Idoso" (65 anos ou mais).
"""

idade = int(input("Digite a idade: "))

if idade <= 12:
    print("Criança")

elif idade >= 13 and idade <= 17:
    print("Adolecente")

elif idade >= 18 and idade <= 64:
    print("Adulto(a)")

elif idade >= 65 and idade <= 150:
    print("Idoso")

else:
    print("Idade inválida")

