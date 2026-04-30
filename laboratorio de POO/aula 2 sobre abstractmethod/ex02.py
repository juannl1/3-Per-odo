#interface segregaion protocal
#protocolo de segregação de Interfaces
from abc import ABC, abstractmethod


class UsuarioBase(ABC):
    @abstractmethod
    def login(self):
        pass

    def logout(self):
        pass

    def alterar_senha(self):
        pass

class AdminBase(UsuarioBase):
    @abstractmethod
    def login(self):
        pass

    def logout(self):
        pass

    def alterar_senha(self):
        pass

    def cadastrar_novos_usuarios(self):
        pass


class Usuario(UsuarioBase):
    def login(self):
        print("Login realizado com sucesso")

    def logout(self):
        print("Logout realizado com sucesso")

    def alterar_senha(self):
        print("Senha alterado com sucesso")

class Admin(AdminBase):
    def login(self):
        print("Login realizado com sucesso")

    def logout(self):
        print("Logout realizado com sucesso")

    def alterar_senha(self):
        print("Senha alterado com sucesso")

    def cadastrar_novos_usuarios(self):
        pass