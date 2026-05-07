from notificador import Notificador

class NotificadorWhatsapp(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando [Whatsapp] com a mensagem: {mensagem}")