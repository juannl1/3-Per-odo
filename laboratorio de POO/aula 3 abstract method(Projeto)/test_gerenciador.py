from gerenciadorNotificacoes import GerenciadorDeNotificacoes
from notificador import Notificador

class NotificadorFake(Notificador):
    def __init__(self):
        self.enviado = False

    def enviar(self, mensagem):
        if len(mensagem) > 0:
            self.enviado = True
        else:
            print("Não enviado")

def test_gerenciador_de_notificacoes():
    n1 = NotificadorFake()
    n2 = NotificadorFake()

    gerenciador = GerenciadorDeNotificacoes([n1, n2])
    gerenciador.enviar_todos("Testando")

    assert n1.enviado is True
    assert n2.enviado is True

 