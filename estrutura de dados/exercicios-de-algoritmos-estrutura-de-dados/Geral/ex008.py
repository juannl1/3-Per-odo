gravidade = float(input("Gravidade do planeta (em relação à Terra): "))
tem_oxigenio = input("Há oxigênio suficiente? (sim/nao): ").lower()

if 0.8 <= gravidade <= 1.2 and tem_oxigenio == "sim":
    print("Planeta habitável! A missão de exploração pode começar.")
else:
    print("Missão abortada. O planeta não atende aos critérios de segurança.")