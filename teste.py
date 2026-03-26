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
            self.valor = 0
            print("Valor inválido, o preço deve ser númerico")
            



lista_de_itens = {
    'mouse_logitech': 549.90,
    'teclado_logitech': 499.90 
}
    
for chave, valor in lista_de_itens.items():
    print(chave, valor)

produto1 = Produto("Memoria Ram", '999')
print(f"{produto1.nome} R$ {produto1.valor}")