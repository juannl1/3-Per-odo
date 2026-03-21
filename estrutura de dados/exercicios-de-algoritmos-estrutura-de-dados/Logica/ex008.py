idade = int(input("Qual a sua idade? "))
atestado = input("Possui atestado médico válido? (sim/nao): ").lower()

if idade < 50 and atestado == "sim":
    print("Inscrição permitida! Você está apto para o evento.")
else:
    print("Inscrição não permitida. Verifique os requisitos de idade ou atestado.")