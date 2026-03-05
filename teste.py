from random import randint


class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self):
        print(f"Vida: {self.vida}")
        print(f"{self.nome} atacou com o braço")
        
class Guerreiro(Personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)                                                                                                     
        self.forca = forca

    def atacar(self):
        
        print(f"Vida: {self.vida}")
        print(f"Força: {self.forca}")
        print(f"Personagem: {self.nome} atacou com o rifle de precisão")
        
        ataque = self.forca - randint(0, 40)
        print(f"Dano: {ataque}")
        print(f"Força de ataque atual: {self.forca - ataque}")

        self.forca = ataque #Atualizando valor



class Mago(Personagem):
    def __init__(self, nome, vida, magia):
        super().__init__(nome, vida)
        self.magia = magia

    def atacar(self):
        print(f"Vida: {self.vida}")
        print(f"Força: {self.magia}")
        print(f"{self.nome} atacou com magia")
    
        ataque = self.magia - randint(0, 40)
        print(f"Dano: {ataque}")
        print(f"Força de ataque atual: {self.magia - ataque}")

        self.magia = ataque #Atualizando valor
        

obj1 = Guerreiro("Joel", 100, 90)
obj2 =  Guerreiro("Batman", 100, 70)



batalhas = 0
while True:
    batalhas += 1
    obj1.forca - obj2






# print("\n----------- Personagem -----------\n")
# obj1.atacar()
# print("\n----------- Guerreiro(Personagem) -----------\n")
# obj2.atacar()
# print("\n----------- Mago(Personagem) -----------\n")
# obj3.atacar()
# print("\n----------- xxxxxxxxxxxxxxxx -----------\n")

