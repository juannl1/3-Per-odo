id_droide = input("Digite o sinal de ID do droide: ").upper()
energia = int(input("Nível de carga de energia (%): "))

if id_droide.startswith("RB") and energia > 70:
    print("Acesso concedido à base rebelde. Bem-vindo, droide!")
else:
    print("Acesso negado. Possível droide de batalha infiltrado!")