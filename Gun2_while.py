#while-else

"""mesai_baslangic=8
mesai_bitis=18

print("İş yeri giriş sistemi")
print("Mesai saatleri: {}:00-{}:00 arasındadır. ".format(mesai_baslangic,mesai_bitis))

while True:
    try:
        saat=int(input("Lütfen giriş saatinizi 24 saat formatında giriniz: "))

        if mesai_baslangic<=saat<=mesai_bitis:
            print("Hoşgeldiniz")
            break
        else: print("Mesai saatleri dışında giriş yapamazsınız.")

    except ValueError:
        print("Hatalı değer girişi yaptınız. Lütfen tekrar deneyiniz.")

    
if saat>=mesai_baslangic and saat<=mesai_bitis:
    pass"""
    
#pass: bir bloğun hiçbir işlem yapmadan geçmesini sağlar
#break: döngüyü sonlandırır
#continue: mevcut döngü sırasını atlayarak döngüyü başa döndürür

"""i=int(input("Bir sayı giriniz: "))

while i<10:
    print(i)
    i+=1
else: print("Girdiğiniz sayı 10'dan küçük değil bu sebeple döngüye girmedi")

sifre="123456"
giris=input("Şifrenizi giriniz: ")

while sifre!=giris:
    print("şifre hatalı,tekrar deneyin")
    giris=input("Şifrenizi giriniz: ")

else: print("Şifre doğrulandı")"""



#1)while break ve continue kullanarak 1-100 arasındaki çift sayıları yazdır. continue kullanımı: herhangi bir çift sayıyı atla

sayi=1

while sayi<=120:

    if sayi%2 != 0:
        sayi+=1
        continue

    if sayi==50:
        sayi+=1
        continue
    
    if sayi==100:
        break

    print(sayi,end=" ")
    sayi+=1

#2)liste oluşturup elemanları while döngüsü ile al ve ekrana yazdır

list1=[]

while True:
    eleman=input("\nListeye eklemek istediğiniz elemanı giriniz('a' ile çıkış yapabilirsiniz): ").lower()
    if eleman=="a":
        break
    list1.append(eleman)

print("Liste elemanları: ",list1)