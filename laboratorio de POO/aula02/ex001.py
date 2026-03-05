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

personagens = []

for q in range(0, 2):
    classePersonagem = int(input("1. Guerreiro \n2. Mago \n\n>>> "))

    nome = str(input("Nome do Personagem: ")).title()
    vida = int(input(f"{nome} possuirá vida: "))

    if classePersonagem == 1:
        forca = int(input(f"{nome} possuirá força: "))
        jogador = Guerreiro(nome, vida, forca)

    elif classePersonagem == 2:
        magia = int(input(f"{nome} possuirá Magia: "))
        jogador = Mago(nome, vida, magia)
    else:
        print("Algo deu errado")

    personagens.append(jogador)
    print("\nJogador criado\n")


player1 = personagens[0]
player2 = personagens[1]

print("------------ Fight ------------")
print(f"{player1.nome} VS {player2.nome}")
while True:
    #Turno 1
    if str(input(f"{player1.nome} deseja atacar? [s/n]: ")).lower in "s":
        ataque = player1.atacar() #Polimorfismo
        player2.vida -= ataque
        print(f"{player2.nome} \nVida: {player2.vida}")
        if player2.vida <= 0:
            print(f"{player2.nome} morreu. \n{player1.nome} Venceu a batalha")
            break

    else:
        print(f"{player1.nome} passou a vez...")


    #Turno 2
    if input(f"{player2.nome} deseja atacar? [s/n]: ") in "Ss":
        ataque = player2.atacar() #Polimorfismo
        player1.vida -= ataque
        print(f"{player1.nome} \nVida: {player1.vida}")
        if player1.vida <= 0:
            print(f"{player1.nome} morreu. \n{player2.nome} Venceu a batalha")
            break

    else:
        print(f"{player2.nome} passou a vez...")

print('--- FIM DE JOGO ---')





#Guerreiro(nome, vida, força)
# personagem = [
#     Guerreiro("Joel", 100, 90),
#     Guerreiro("Batman", 100, 70),
#     Mago("Mago do Clash Royale", 100, 50)
# ]

# for p in personagem: # Poliforfismo de uma forma que eu nunca vi
#     p.atacar()
#     print("\n", 20*"=-", "\n")






# obj1 = Personagem("Joel", randint(1, 100))
# obj2 = Guerreiro("Ellie", randint(1, 100), randint(1, 100))
# obj3 = Mago("Walter White", randint(1, 100), randint(1, 100))
# print("\n----------- Personagem -----------\n")
# obj1.atacar()
# print("\n----------- Guerreiro(Personagem) -----------\n")
# obj2.atacar()
# print("\n----------- Mago(Personagem) -----------\n")
# obj3.atacar()
# print("\n----------- xxxxxxxxxxxxxxxx -----------\n")

