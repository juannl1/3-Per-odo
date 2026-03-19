"""
Maior de Três Números: Desenvolva um programa que recebe três números
diferentes do usuário e determina qual é o maior deles
"""

numero1 = int(input("1° Número: "))
numero2 = int(input("2° Número: "))
numero3 = int(input("3° Número: "))

if numero1 > numero2 and numero1 > numero3:
    print("O número 1° é maior")

elif numero2 > numero1 and numero2 > numero3:
    print("O número 2° é maior")

elif numero3 > numero2 and numero3 > numero1:
    print("O número 3° é maior")

else:
    print("Os números são iguais")

