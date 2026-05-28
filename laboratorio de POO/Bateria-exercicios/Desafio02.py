from abc import ABC as abc, abstractmethod

class PublicadorConteudo:

    def publicar_video(self):
        pass

    def transmitir_ao_vivo(self):
        pass


class CursoGravado(PublicadorConteudo):

    def publicar_video(self):
        print("Vídeo publicado")

class Aovivo:
    def transmitir_ao_vivo(self):
        print("Transmitindo AOVIVO")

class Database(abc):
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

class NotificadorDoSistema(abc):
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

curso = CursoGravado()
curso_aovivo = Aovivo()

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