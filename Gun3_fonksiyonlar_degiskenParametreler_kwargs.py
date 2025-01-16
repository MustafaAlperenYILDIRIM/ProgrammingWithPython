#args: Birden fazla parametreyi almayı sağlar, parametre sayısı değişken olabilir.
def toplama(*degerler):
    toplam=0
    for i in degerler:
        toplam+=i
    return toplam
degerler= []

adet=int(input("kaç adet değer gireceksiniz?:"))

for i in range(adet):
    deger=int(input("{}. değeri giriniz:" .format(i+1)))
    degerler.append(deger)

print("Toplama işleminin sonucu:{}" .format(toplama(*degerler)))



#KWARGS
def bilgi_goster(**kwargs):
    for anahtar, deger in kwargs.items():
        print(f"{anahtar}: {deger}")


bilgi_goster(isim="Ahmet", yas=25, meslek="Mühendis")

