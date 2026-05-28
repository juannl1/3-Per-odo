from abc import ABC, abstractmethod

class PublicadorConteudo(ABC):
    @abstractmethod
    def publicar_video(self):
        pass

class Aovivo(ABC):
    @abstractmethod
    def transmitir_ao_vivo(self):
        pass

class Video(PublicadorConteudo):

    def publicar_video(self):
        print("Vídeo publicado")

class Transmissao(Aovivo):
    def transmitir_ao_vivo(self):
        print("Transmitindo AOVIVO")

class Database(ABC):
    @abstractmethod
    def conectar(self):
        pass

class MySQLDatabase(Database):
    def conectar(self):
        print("Conectado ao MySQL")


class PlataformaCursos:
    def __init__(self, database: Database):
        self.database = database

    def salvar_curso(self):
        self.database.conectar()
        print("Curso salvo")

class NotificadorDoSistema(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

class NotificadorEmail(NotificadorDoSistema):
    def enviar(self, mensagem):
        return f"EMAIL: {mensagem}"
    
class NotificadorSMS(NotificadorDoSistema):
    def enviar(self, mensagem):
        return f"SMS: {mensagem}"
    
class NotificadorPUSH(NotificadorDoSistema):
    def enviar(self, mensagem):
        return f"PUSH: {mensagem}"

#Exemplo de Uso
# =====================================
# PUBLICAÇÃO DE CURSOS
# =====================================

curso = Video()
curso_aovivo = Transmissao()

curso.publicar_video()

# Problema:
curso_aovivo.transmitir_ao_vivo()


# =====================================
# PLATAFORMA
# =====================================
banco_mysql = MySQLDatabase()
plataforma = PlataformaCursos(banco_mysql)

plataforma.salvar_curso()


# =====================================
# NOTIFICAÇÕES
# =====================================

notificador1 = NotificadorEmail()
notificador2 = NotificadorPUSH()
notificador3 = NotificadorSMS()

print(notificador1.enviar("Novo curso disponível!"))
print(notificador2.enviar("Sua matrícula foi confirmada!"))
print(notificador3.enviar("Sua matrícula foi confirmada!"))