# Coleta de credenciais do oficial
autorizacao = input("Digite seu nível de autorização: ").strip().title()
senha = input("Digite a senha de acesso: ")

# Verificação dos protocolos da Federação
if autorizacao == "Top Secret" and senha == "ST1234":
    print("Acesso concedido. Carregando arquivos sobre tecnologia Klingon...")
else:
    print("Acesso negado. Tentativa de acesso não autorizada registrada.")