class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


a = Singleton()
b = Singleton()
print(a == b)

class t:
    def __init__(self):
        pass

t1=t()
t2=t()
print(t1==t2)


class Observer:
    def update(self, mesaj):
        pass

class Abone(Observer):
    def __init__(self, isim):
        self.isim = isim

    def update(self, mesaj):
        print(f"{self.isim}, yeni mesaj: {mesaj}")

class Yayinci:
    def __init__(self):
        self.aboneler = []

    def abone_ekle(self, abone):
        self.aboneler.append(abone)

    def bildirim_gonder(self, mesaj):
        for abone in self.aboneler:
            abone.update(mesaj)

# Kullanım
abone1 = Abone("Ali")
abone2 = Abone("Ayşe")

yayinci = Yayinci()
yayinci.abone_ekle(abone1)
yayinci.abone_ekle(abone2)

yayinci.bildirim_gonder("Yeni makale yayınlandı!")


def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def metin():
    return "Merhaba Dünya!"

print(metin())
