nivel_credencial = int(input("Qual o seu nível de credencial? "))
quantidade_guardas = int(input("Quantos guardas estão acompanhando? "))

if nivel_credencial >= 5 and quantidade_guardas >= 2:
    print("Acesso concedido à conferência")
else:
    print("Acesso negado")