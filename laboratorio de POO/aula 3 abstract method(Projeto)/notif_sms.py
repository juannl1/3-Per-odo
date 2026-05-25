from notificador import Notificador
from typing import List, Optional
from usuario import Usuario


class NotificadorSMS(Notificador):
    def enviar(self, mensagem: str, destinatarios: Optional[List[Usuario]] = None):
        #Simulação de envio via SMS

        if not destinatarios:
            print(f"[SMS] Simulação: {mensagem}")

        print(f"[SMS] - Simulando envio para {len(destinatarios)} destinatários")
        for usuario in destinatarios:
            print(f"[SMS] simulado para {usuario.contato}: {mensagem}")

    def obter_tipo(self) -> str:
        return "Sms"