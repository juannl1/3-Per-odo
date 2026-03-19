"""
Par ou Ímpar: Desenvolva um programa que recebe um número inteiro e
imprime "Par" se o número for par ou "Ímpar" se for ímpar.
"""

numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print(f"{numero} é par")
else:
    print(f"{numero} é impar")

