"""from abc import ABC, abstractmethod


class Odeme(ABC):
    @abstractmethod
    def Ode(self, miktar):
        pass  


class KrediKartiOdeme(Odeme):
    def Ode(self, miktar):
        return f"Kredi kartıyla {miktar} TL ödendi."


class NakitOdeme(Odeme):
    def Ode(self, miktar):
        return f"Nakit olarak {miktar} TL Odendi."


Odeme1 = KrediKartiOdeme()
print(Odeme1.Ode(100)) 

Odeme2 = NakitOdeme()
print(Odeme2.Ode(50))  """

from abc import ABC, abstractmethod

#Soyut sınıf
class Sekil(ABC):

    @abstractmethod
    def alan_hesapla(self):
        pass

    @abstractmethod
    def cevre_hesapla(self):
        pass

#Alt sınıf 
class Daire(Sekil):

    def __init__(self,r):
        self.r=r
    
    def alan_hesapla(self):
        return 3.14*self.r**2
    def cevre_hesapla(self):
        return 2*3.14*self.r
    
class Dikdortgen(Sekil):
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def alan_hesapla(self):
        return self.a*self.b
    
    def cevre_hesapla(self):
        return 2*(self.a+self.b)


sekil=Sekil()

daire=Daire(3)
print("Daire alanı:{}, çevresi:{}".format(daire.alan_hesapla(),daire.cevre_hesapla()))

dikdortgen=Dikdortgen(3,4)
print("Dikdörtgen alanı:{}, çevresi:{}".format(dikdortgen.alan_hesapla(),dikdortgen.cevre_hesapla()))