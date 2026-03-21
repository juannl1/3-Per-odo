idade = int(input("Qual é a sua idade? "))
acompanhado = input("Está acompanhado por um adulto? (sim/nao): ").lower()

if idade > 70 or (idade < 12 and acompanhado == "sim"):
    print("Você pode assistir ao cinema gratuitamente!")
else:
    print("O ingresso não é gratuito.")