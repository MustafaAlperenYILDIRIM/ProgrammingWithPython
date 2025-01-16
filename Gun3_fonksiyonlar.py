"""
#Basit Fonksiyon Örneği

def merhaba_dunya():
    print("Merhaba Dünya!")

merhaba_dunya()


#Paremetre Alan Fonskiyon Örneği
def topla(a, b):
    return a + b

print(topla(1, 3))"""

#fonksiyon ile if-else ifadesi kullanalım-girilen sayı 10dan büyük mü veya 20 den büyük mü yoksa hiçbiri değil mi? if-elif-else


sayi_kontrol=lambda x: "10'dan büyük" if x>=10 and x<=20 else "20'den büyük" if x>20 else "Hiçbiri değil" 

kontrol=lambda y: "10'dan küçük" if y<10 else(
    "10 ile 20 arasında" if 10<=y<20 else(
        "20 ile 30 arasında" if 20<=y<30 else "30'dan büyük"
    )
)

sayi=int(input("Bir sayı giriniz:"))
print(kontrol(sayi))

kare= lambda y:y**2
a=int(input("bir sayı giriniz:"))
print(kare(a))

#lambda fonksiyonu ile iki sayının toplama işlemini yaptıralım 


#10:30'da görüşmek üzere