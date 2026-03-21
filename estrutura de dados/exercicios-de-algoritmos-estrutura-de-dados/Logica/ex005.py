score = input("Digite seu score (ótimo, bom, regular): ").lower()
valor = float(input("Digite o valor do empréstimo: R$ "))


if score == "ótimo":
    taxa = 5 if valor > 5000 else 7
elif score == "bom":
    taxa = 10 if valor > 5000 else 12
elif score == "regular":
    taxa = 15 if valor > 5000 else 18
else:
    taxa = None

if taxa:
    print(f"A taxa de juros será de {taxa}% ao mês.")
else:
    print("Score inválido!")