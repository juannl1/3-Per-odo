from notificador import Notificador
from usuario import Usuario
from typing import List, Optional
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os
import smtplib



class NotificadorEmail(Notificador):
    def __init__(self, smtp_server: str = None, smpt_port: int = None, email_remetente: str = None, senha: str = None):
        pass
                                                                                                     