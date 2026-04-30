from abc import ABC, abstractmethod

class TrabalhadorBase(ABC):
    @abstractmethod
    def trabalhar(self):
        pass

    def comer(self):
        pass

    def dormir(self):
        pass

class RoboBase(TrabalhadorBase):
    @abstractmethod
    def trabalhar(self):
        pass

class HumanoTrabalhador(TrabalhadorBase):
    def trabalhar(self):
        print("Humano está trabalhando")

    def comer(self):
        print("Humano está se alimentando")

    def dormir(self):
        print("Humano está dormindo")


class RoboTrabalhador(RoboBase):
    def trabalhar(self):
        print("Robo está trabalhando")
 
HumanoTrabalhador().trabalhar()
HumanoTrabalhador().dormir()
HumanoTrabalhador().comer()
RoboTrabalhador().trabalhar()
