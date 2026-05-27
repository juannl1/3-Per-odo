from abc import ABC, abstractmethod

class Pedido:
    def __init__(self, cliente: str, tipo_entrega: str):
        self.cliente = cliente
        self.tipo_entrega = tipo_entrega
        self.itens = []
        self.total = 0

    def adicionar_item(self, nome: str, preco: float):
        self.itens.append((nome, preco))
        self.total += preco
    
class Desconto(ABC):
    @abstractmethod
    def descontar(total):
        pass

class DescontoComum(Desconto):
    def descontar(total):
        return total * 0.95
    
class DescontoVip(Desconto):
    def descontar(total):
        return total * 0.8
    
class DescontoFuncionario(Desconto):
    def descontar(total):
        return total * 0.5
    
class TipoEntrega(ABC):
    @abstractmethod
    def realizar_entrega():
        pass

class EntregaMotoboy(TipoEntrega):
    def realizar_entrega():
        return "Entrega realizada por motoboy"
    
class EntregaTransportadora(TipoEntrega):
    def realizar_entrega():
        return "Entrega realizada por transportadora"
    
class Retirada(TipoEntrega):
    def realizar_entrega():
        print("Retirada não realiza entrega")

class PedidoRepository:
    def salvar_no_banco(cliente):
        print(f"Salvando pedido de {cliente} no banco")

class EmailService:
    def enviar_email_confirmacao(cliente):
        print(f"Enviando email para {cliente}")

class RelatorioPedido:
    def gerar_relatorio(itens):
        print("======== RELATÓRIO ========")
        for item in itens:
            print(item)


#------------------------------------------------------------
#Exemplos de Uso:
pedidos = [Pedido("Tiago", "retirada"), Pedido("Juan", "Retirada")]

for pedido in pedidos:
    pedido.adicionar_item("Notebook", 3500)
    pedido.adicionar_item("Mouse Gamer", 250)

    print(f"Total antes do desconto: R$ {pedido.total}")

    print(f"Total com desconto VIP: R$ {DescontoVip.descontar(pedido.total)} \nTotal com desconto Comum: R$ {DescontoComum.descontar(pedido.total)} \nTotal com desconto Funcionário: R$ {DescontoFuncionario.descontar(pedido.total)}")

    print(f"Total com desconto: R$ {pedido.total}")

    PedidoRepository.salvar_no_banco(pedido.cliente)

    EmailService.enviar_email_confirmacao(pedido.cliente)

    RelatorioPedido.gerar_relatorio(pedido.itens)

    print(EntregaMotoboy.realizar_entrega())
print("finalizado")