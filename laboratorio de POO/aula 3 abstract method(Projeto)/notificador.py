from abc import ABC, abstractmethod 
from typing import List, Optional
from usuario import Usuario


class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem: str, destinararios: Optional[List[Usuario]] = None):
        pass

    @abstractmethod
    def obter_tipo(self) -> str:
        # Retorna o tipo da plataforma (Email, SMS, ZAP)
        pass

