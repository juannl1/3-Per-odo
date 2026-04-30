from abc import ABC, abstractmethod

#DIP = Dependency Injection Principle
#Injecção de dependencia é um padrão de design

class Enviador(ABC):
    @abstractmethod
    def enviar(self, contato):
        pass
    
class EnviadorEmail(Enviador):
    def enviar(self, contato):
        #Logica de envio
        print(f"Email enviado para {contato}")

class EnviadorZap(Enviador):
    def enviar(self, contato):
        #Logica de envio
        print(f"Zap enviado para {contato}")

class EnviadorSMS(Enviador):
    def enviar(self, contato):
        print(f"SMS enviado para {contato}")
    
class CadastroUsuario:
    def __init__(self, enviador: Enviador):
        self.enviador = enviador
        self.nome = str()

    def cadastrar(self, nome, email):
        #Logica de cadastro
        self.enviador.enviar(email)
        self.nome = nome
        print(f"Email enviado para {nome}")

#implementação


while True:
    try:
        print("=========== Enviador ===========")
        nome = str(input("Nome: ")).title()
        email = str(input("Email: "))
        telefone = int(input("Telefone: "))

        opcoes = int(input("[1] - SMS \n[2] - Whatsapp \n[3] - Email \nVocê deseja receber em qual forma: "))
        if opcoes == 1:
            enviador = EnviadorSMS()
            cadastro = CadastroUsuario(enviador)
            cadastro.cadastrar(nome, telefone)
        elif opcoes == 2:  
            enviador = EnviadorZap()
            cadastro = CadastroUsuario(enviador)
            cadastro.cadastrar(nome, telefone)

        elif opcoes == 3:
            enviador = EnviadorEmail()
            cadastro = CadastroUsuario(enviador)
            cadastro.cadastrar(nome, email)
        
        elif opcoes == 0:
            break
        else:
            print("Valor inválido")
    except ValueError:
        print("\n\nErro\n")


        
