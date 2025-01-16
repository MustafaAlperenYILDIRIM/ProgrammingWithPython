#immutable-değerle döndürme:

def değiştir(x):
    x += 5 #x=x+5
    print("Fonksiyon içi x:", x)

sayı = 10
değiştir(sayı)
print("Fonksiyon dışı sayı:", sayı)

#mutable-referansla döndürme:

def ekle(list1):
    list1.append(4)
    print("Fonksiyon içi liste:",list1)


liste=[1,2,3]

ekle(liste)
print("Fonksiyon dışı liste:",liste)


