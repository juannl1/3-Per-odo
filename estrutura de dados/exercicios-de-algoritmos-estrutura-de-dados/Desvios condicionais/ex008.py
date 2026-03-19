"""
Temperatura Ideal: Implemente um programa que recebe uma temperatura
em graus Celsius. Baseado no valor, classifique e imprima se está "Muito
frio" (abaixo de 5ºC), "Frio" (5ºC a 15ºC), "Agradável" (16ºC a 25ºC),
"Quente" (26ºC a 35ºC), ou "Muito quente" (acima de 35ºC).
"""


temperatura = int(input("Digite a temperatura em Celsius: "))

if temperatura <= 5:
    print(f"Muito frio {temperatura}")

elif temperatura > 5 and temperatura < 15:
    print("Frio")

elif temperatura >= 16 and temperatura < 25:
    print("Agradável")

elif temperatura >= 26 and temperatura < 35:
    print("Quente")

elif temperatura >= 35 and temperatura <= 60:
    print("Muito Quente")
else:
    print("Temperatura inválida")