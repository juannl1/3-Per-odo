from notificador import Notificador
from typing import List, Optional
from usuario import Usuario

class NotificadorWhatsapp(Notificador):
    def enviar(self, mensagem: str, destinatarios: Optional[List[Usuario]] = None):
        #Simulação de envio via ZAP

        if not destinatarios:
            print(f"[ZAP] Simulação: {mensagem}")

        print(f"[ZAP] - Simulando envio para {len(destinatarios)} destinatários")
        for usuario in destinatarios:
            print(f"[ZAP] simulado para {usuario.contato}: {mensagem}")

    def obter_tipo(self) -> str:
        return "Zap"