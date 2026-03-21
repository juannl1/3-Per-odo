temp = float(input("Digite a temperatura atual em °C: "))

if temp > 35 or temp < 0:
    print("ALERTA: Condições climáticas extremas!")
else:
    print("Temperatura dentro da normalidade.")