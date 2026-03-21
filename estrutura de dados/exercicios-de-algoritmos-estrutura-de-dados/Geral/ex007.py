# Coleta de dados do Padawan
horas_sabre = int(input("Quantas horas de treinamento com sabre de luz você completou? "))
recomendacao_mestre = input("Você possui a recomendação do seu mestre Jedi? (sim/nao): ").lower()

# Verificação dos requisitos para avançar
if horas_sabre >= 500 and recomendacao_mestre == "sim":
    print("Você está qualificado para avançar em seu treinamento Jedi. Que a Força esteja com você!")
else:
    print("Ainda não é o momento. Continue seu treinamento e busque a sabedoria de seu mestre.")