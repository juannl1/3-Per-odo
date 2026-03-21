usuario_correto = "usuario"
senha_correta = "senha123"

user = input("Digite o nome de usuário: ")
password = input("Digite a senha: ")

if user == usuario_correto and password == senha_correta:
    print("Acesso permitido! Bem-vindo.")
else:
    print("Usuário ou senha incorretos.")