"""
Aprovado ou Reprovado: Crie um programa que pede ao usuário para inserir
a nota final em uma disciplina. Se a nota for igual ou superior a 70, imprima
"Aprovado". Caso contrário, imprima "Reprovado
"""


nota = float(input("Digite a nota [0 a 100]: "))

if nota >= 70.0:
    print(f"Aprovado(a) !!! \nNota: {nota}/100")

elif nota < 70.0:
    print(f"Reprovado(a) \nNota: {nota}/100")
    
else:
    print("Insira uma nota válida")