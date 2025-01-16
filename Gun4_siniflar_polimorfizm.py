
class Sekil:
    def alan_hesapla(self):
        pass


class Dikdortgen(Sekil):
    def __init__(self, uzunluk, genislik):
        self.uzunluk = uzunluk
        self.genislik = genislik

    def alan_hesapla(self):
        return self.uzunluk * self.genislik


class Daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap

    def alan_hesapla(self):
        return 3.14 * self.yaricap ** 2


dikdortgen = Dikdortgen(5, 3)
daire = Daire(7)

sekiller = [dikdortgen, daire]


for i in sekiller:
    print(f"Alan: {i.alan_hesapla()}")


class arac:
    def hareket_et(self):
        pass

class bot(arac):
    def __init__(self,marka,model):



"""class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()"""