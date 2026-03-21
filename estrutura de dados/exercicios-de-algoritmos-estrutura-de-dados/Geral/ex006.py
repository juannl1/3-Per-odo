poder = input("Qual a classificação do seu superpoder (S, A, B, C)? ").upper()
planeta_hostil = input("Você reside em um planeta considerado hostis? (sim/nao): ").lower()

if (poder == "S" or poder == "A") and planeta_hostil == "nao":
    print("Candidatura aceita! Você será avaliado pela Liga da Justiça.")
else:
    print("Candidatura negada. Requisitos de poder ou origem não atendidos.")