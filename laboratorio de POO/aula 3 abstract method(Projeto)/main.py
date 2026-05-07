from notificadorEmail import NotificadorEmail
from notificadorLOG import NotificadorLog
from notificadorSMS import NotificadorSMS
from notificadorWhatsapp import NotificadorWhatsapp
from gerenciadorNotificacoes import GerenciadorDeNotificacoes

email = NotificadorEmail()
sms = NotificadorSMS()
whatsapp = NotificadorWhatsapp()

log = NotificadorLog()

notificadores = [email, sms, whatsapp, log]
gerenciador = GerenciadorDeNotificacoes(notificadores)

pergunta = str(input("Mensagem > > > "))

gerenciador.enviar_todos(pergunta)
