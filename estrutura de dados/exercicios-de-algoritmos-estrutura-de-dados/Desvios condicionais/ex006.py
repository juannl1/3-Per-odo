"""
Classificação de Filmes: Desenvolva um programa que, baseado na idade
inserida pelo usuário, informe se a pessoa está autorizada a assistir a um
filme classificado como R (restrito a maiores de 18 anos).
"""

idade = int(input("Digite a idade: "))

if idade <= 18:
    print("Este filme tem a classificação indicativa R (+18)")
else:
    ''