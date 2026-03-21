codigo = input("Digite seu código de acesso: ").upper()
avaliacao = int(input("Digite sua avaliação de combate (0-100): "))

if codigo.endswith("A") and avaliacao >= 80:
    print("Acesso concedido ao QG dos Vingadores. Avante!")
else:
    print("Acesso negado. Identidade não confirmada ou nível insuficiente.")