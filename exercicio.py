class Conta:
    def __init__(self):
        self.saldo = 0


    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, (int, float)) and valor > 0:
            self.__saldo = valor
            print("Sucesso !")

        else:
            self.saldo += 0
            raise ValueError("Não foi possivel efetuar a transação")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R$ {valor} realizado com sucesso")
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor} Realizado com sucesso")
            print(f"Seu novo saldo é R$ {self.saldo}")

        else:
            print("Saldo insuficiente para saque")




while True:
    print(30*"=", "Banco", 30*"=")
    try:
        pergunta = int(input("[1] - Depositar \n[2] - Sacar \n[3] - Ver saldo \n[0] - Sair \n\nDigite sua opção: "))
    
    except:
        


