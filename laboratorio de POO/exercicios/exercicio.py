class Conta:
    def __init__(self):
        self.saldo = 0


    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self.__saldo = valor

        else:
            self.saldo += 0
            raise ValueError("Não foi possivel efetuar a transação")



    def depositar(self, valor):

        self.saldo += valor
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso")
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} Realizado com sucesso")
            print(f"Seu novo saldo é R$ {self.saldo:.2f}")

        else:
            print("Saldo insuficiente para saque")


conta1 = Conta()

while True:
    print(30*"=", "Banco", 30*"=")
    try:
        print(f"\nSeu saldo: {conta1.saldo}")
        pergunta = int(input("[1] - Depositar \n[2] - Sacar \n[3] - Consultar saldo \n[0] - Sair \n\nDigite sua opção: "))

        if pergunta == 1:
            print(30 * "=", "Depositar", 30 * "=")
            print(f"\n\nSeu saldo: {conta1.saldo}\n")
            valor = float(input("Qual o valor que você deseja depositar: "))
            
            conta1.depositar(valor)

            print(f"\nSeu saldo atualizado: {conta1.saldo}\n")

        
        elif pergunta == 2:
            print(30 * "=", "Sacar", 30 * "=")
            print(f"\n\nSeu saldo: {conta1.saldo}\n")
            valor = float(input("Qual o valor do saque: "))
            
            conta1.sacar(valor)

            print(f"\nSeu saldo atualizado: {conta1.saldo}\n")

        elif pergunta == 3:
            print(30 * "=", "Consultar saldo", 30 * "=")
            print(f"\n\nSeu saldo: {conta1.saldo}\n")

            print(f"\nSeu saldo atualizado: {conta1.saldo}\n")

        elif pergunta == 0:
            print("Saindo...")
            break

    except ValueError:
        print("Inválido. Tente novamente")