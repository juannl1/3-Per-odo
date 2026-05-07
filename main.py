from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

class NotificadorEmail(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando [Email] com a mensagem: {mensagem}")

class NotificadorSMS(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando [SMS] com a mensagem: {mensagem}")

class NotificadorLog(Notificador):
    def enviar(self, mensagem):
        with open("log.JSON", "a") as file:
            file.write(f"[ LOG ] {mensagem} \n")

class GerenciadorDeNotificacoes:
    def __init__(self, notificadores: list[Notificador]):
        self.notificadores = notificadores

    def enviar_todos(self, mensagem):
        for notificador in self.notificadores:
            notificador.enviar(mensagem)



email = NotificadorEmail()
sms = NotificadorSMS()
log = NotificadorLog()

notificadores = [email, sms, log]
gerenciador = GerenciadorDeNotificacoes(notificadores)

pergunta = str(input("Mensagem > > > "))

gerenciador.enviar_todos(pergunta)
