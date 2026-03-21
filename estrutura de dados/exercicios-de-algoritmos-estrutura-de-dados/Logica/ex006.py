idade = int(input("Qual a sua idade? "))
curso = input("Completou o curso de direção? (sim/nao): ").lower()

if idade >= 18 and curso == "sim":
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir.")