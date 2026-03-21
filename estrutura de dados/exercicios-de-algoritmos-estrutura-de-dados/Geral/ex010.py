temperatura = float(input("Qual a temperatura externa (°C)? "))
alerta_maximo = input("A polícia está em alerta máximo? (sim/nao): ").lower()
uso_recente = int(input("Há quantos dias você usou este disfarce? "))

if temperatura < 5 and alerta_maximo == "nao" and uso_recente > 30:
    print("Disfarce autorizado. Lupin desapareceu na névoa!")
else:
    print("Risco muito alto! Lupin deve encontrar outra rota de fuga.")