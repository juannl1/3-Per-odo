class Modificador:
    @staticmethod
    def maiusculo(nome):
        return nome.upper()
    
    @staticmethod
    def tirando_espacoes(nome):
        return nome.strip()

    @staticmethod
    def minusculo(nome):
        return nome.lower()

    @staticmethod
    def primeira_maiuscula(nome):
        return nome.capitalize()
    
    @staticmethod
    def formatacao_title(nome):
        return nome.title()


class Produto:
    def __init__(self, nome, valor):
        self.valor = valor
        self.nome = nome

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, novo_valor):
        if isinstance(novo_valor, (int, float)) and novo_valor >= 0:

            self.__valor = novo_valor

        else:
            self.__valor = 0
            print("Valor inválido, o preço deve ser númerico")





nome_produto = str(input("Digite o nome do produto: "))

nomesModificados = {
    'maiusculo': Modificador.maiusculo(nome_produto),
    'minusculo': Modificador.minusculo(nome_produto),
    'primeira_maiuscula': Modificador.primeira_maiuscula(nome_produto),
    'formatacao_title': Modificador.formatacao_title(nome_produto),
    'tirando_espacos': Modificador.tirando_espacoes(nome_produto)
}

while True:
    pergunta = int(input("[1] - Letras Maiusculas \n[2] - Letras Minusculas \n[3] - Capitalizar \n[4] - Remover espaços \n[5] - Formatação Title \n[0] - sair \n\nEscolha uma opção abaixo: "))

    if pergunta == 1:
        print(nomesModificados['maiusculo'])

    elif pergunta == 2:
        print(nomesModificados['minusculo'])

    elif pergunta == 3:
        print(nomesModificados['primeira_maiuscula'])

    elif pergunta == 4:
        print(nomesModificados['tirando_espacos'])

    elif pergunta == 5:
        print(nomesModificados['formatacao_title'])

    elif pergunta == 0:
        print("Saindo")
        break
    else:
        print("Entrada inválida")


print(30*"=")
print("Todos as opções")
for chave, valor in nomesModificados.items():
    print(f"{chave} --> {valor}")
print(30*"=")





#