"""
Comparação de Idades: Escreva um programa que solicita ao usuário para
inserir duas idades diferentes. O programa deve imprimir qual das duas é
maior ou se ambas são iguais.
"""

idade1 = int(input("1° Idade >>> "))
idade2 = int(input("2° Idade >>> "))

if idade1 == idade2:
    print("As idades são iguais")
elif idade1 > idade2:
    print("A 1° pessoa é mais velha")
else:
    print("A 2° pessoa é mais velha")