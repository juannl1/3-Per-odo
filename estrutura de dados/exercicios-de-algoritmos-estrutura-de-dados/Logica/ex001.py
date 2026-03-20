"""
Classificação por Altura e Idade: Implemente um programa que recebe a
altura (em metros) e a idade de uma pessoa. Verifique se ela pode entrar em
um brinquedo que requer altura mínima de 1,40m e idade mínima de 12 anos.
Imprima a permissão ou restrição.
"""

idade = int(input("Digite a idade: "))
altura = float(input("Digite a altura em metros ex:[1.80]: "))

if idade >= 12 and altura >= 1.40:
    print("Permissão concedida...")
else:
    print(f"Permissão negada... \nMinimo: 1.40 \nSua altura: {altura:.2f}")


