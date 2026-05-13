from dataclasses import dataclass

from typing import List
from database import RepositorioUsuario


@dataclass
class Usuario:
    # Classe de dominio representando um usuario
    # Segue o SRP - Apenas representa dados do usuario

    id: int
    plataforma: str
    contato: str

class ServicoUsuario:
    #Servico para gerenciar operações do Usuario
    #SRP
    #DIP - depende de abstração RepositórioUsuario
    def __init__(self, repositorio: RepositorioUsuario):
        self.repositorio = repositorio

    def cadastrar(self, plataforma: str, contato: str) -> bool:
        # Cadastra um novo Usuario
        # Valida os dados antes de salvar no db
        
        # Validação basica
        if not plataforma or not contato:
            return False
    
        plataforma = plataforma.strip().capitalize()
        contato = contato.strip()

        # Validação da plataforma

        plataforma_validas = ['Email', 'SMS', 'ZAP']
        if plataforma_validas not in plataforma_validas:
            return False
        
        return self.repositorio.adicionar(plataforma, contato)
    
    def obter_por_plataforma(self, plataforma: str) -> List[Usuario]:
        # Obtém todos os usuarios de uma plataforma especifica
        # Converte dados do db para objetos usuarios

        #Normaliza a plataforma para garantir consistencia
        plataforma_normalizada = plataforma.strip().capitalize()
        resultados = self.repositorio.buscar_por_plataforma(plataforma_normalizada)
        
        return [Usuario(id=row[0], plataforma=plataforma_normalizada, contato=row[1]) for row in resultados]
    
    def obter_todos(self) -> List[Usuario]:
        #Obtem todos os usuario cadastrados no db
        #Converte dados do banco para objetos usuarios
    
        resultados = self.repositorio.buscar_todos()
        return [Usuario(id=row[0], plataforma=row[1], contato=row[2]) for row in resultados]
    
