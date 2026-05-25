from notificador import Notificador
from usuario import Usuario
from typing import List, Optional
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os
import smtplib



class NotificadorEmail(Notificador):
    def __init__(self, smtp_server: str = None, smpt_port: int = None, email_remetente: str = None, senha: str = None):
        # Inicializa o notificador Email se fornecido,
        # Se não, tenta obter das variaveis de ambiente.

        self.smtp_server = smtp_server or os.getenv("SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = smpt_port or int(os.getenv("SMTP_PORT", "587"))
        self.email_remetente = email_remetente or os.getenv("EMAIL_REMETENTE", "")
        self.senha = senha or os.getenv("EMAIL_SENHA", "")

    def obter_tipo(self) -> str:
        return "Email"

    def enviar(self, mensagem: str, destinatarios: Optional[List[Usuario]] = None):
        #Envia email para os destinatários fornecidos
        #Se os destinatarios for None apenas imprime (Modo simulação)

        if not destinatarios:
            print(f"[Email] simulação: {mensagem}")
            return
        
        if not self.email_remetente or not self.senha:
            print(f"[Email] Configuração não encontrada")
            print("[Email] Configure EMAIL_REMETENTE e EMAIL_SENHA no arquivo .env")

            for usuario in destinatarios:
                print(f"-> Email Simulado para {usuario.contato}: {mensagem}")
                return
            
        #Envio real

        try:
            servidor = smtplib.SMTP(self.smtp_server, self.smtp_port)
            servidor.starttls()
            servidor.login(self.email_remetente, self.senha)

            for usuario in destinatarios:
                msg = MIMEMultipart()
                msg["From"] = self.email_remetente
                msg["To"] = usuario.contato
                msg["Subject"] = "Notificação do Sistema"
                msg.attach(MIMEText(mensagem, "plain", "utf-8"))

                servidor.send_message(msg)
                print(f"[EMAIL] enviado para {usuario}")
            
            servidor.quit()

        except Exception as e:
            print(f"[EMAIL] Erro ao enviar: {e}")
            print(f"[EMAIL] Simulado Enviado para {len(destinatarios)}")
            for usuario in destinatarios:
                print(f"Email simulado para {usuario.contato}: {mensagem}")







