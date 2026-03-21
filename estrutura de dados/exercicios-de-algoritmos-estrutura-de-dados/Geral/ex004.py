sensor1 = input("O sensor 1 está desativado? (sim/nao): ").lower()
sensor2 = input("O sensor 2 está desativado? (sim/nao): ").lower()
minutos = int(input("Quantos minutos se passaram das 3h da manhã? "))

if sensor1 == "sim" and sensor2 == "sim" and 0 <= minutos <= 15:
    print("Condições ideais. Lupin pode proceder com o plano!")
else:
    print("Plano abortado. Os riscos de ser capturado são muito altos!")