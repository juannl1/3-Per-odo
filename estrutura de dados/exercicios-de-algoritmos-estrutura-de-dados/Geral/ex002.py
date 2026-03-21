velocidade = float(input("Velocidade atual (km/s): "))
escudo_ativo = input("Escudo de radiação ativo? (sim/nao): ").lower()

if 99000 <= velocidade <= 101000 and escudo_ativo == "sim":
    print("Condições ideais. A nave pode entrar no wormhole!")
else:
    print("Acesso negado. Risco de desintegração da nave!")