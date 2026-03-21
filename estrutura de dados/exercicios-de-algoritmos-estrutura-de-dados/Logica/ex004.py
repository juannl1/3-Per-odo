"""
Desconto na Compra: Implemente um programa que calcula se uma compra
de um número de itens superior a 100 e um valor total superior a 500 reais é
elegível para um desconto de 10%
"""


print("==================== KABUM ====================\n\n")

valores = []
i = 0
while True:
    i += 1
    print("\n****Digite 0 quando acabar as compras****\n")
    valor = float(input(f"Digite o valor {i}° da compra: "))

    valores.append(valor)

    if valor == 0:
        print("\n\n\nFinalizado carrinho...\n")
        total = sum(valores)
        print(f"TOTAL: {total}")
        break

encontrei = False
for n in valores:
    if n > 100:
        encontrei = True
        break

if encontrei == True and total >= 500:
    print("\nVocê recebeu um desconto de 10% na sua compra")
    
    total = total - (0.10 ** 500)
    print(f"\nTotal com desconto: {total}")

else:
    ''
