tahmin=int(input("5-10 arasında bir sayı tahmin edin: "))


if tahmin==6:
    print("Tebrikler doğru tahmin!")

elif tahmin==7:
    print("Tahmin: 7, Yaklaştınız!")

elif tahmin==8:
    print("Tahmin: 8, Yaklaştınız!")

elif tahmin==9:
    print("Tahmin: 9, Uzak!")

elif tahmin>10 or tahmin<5:
    print("Hatalı değer, 5-10 arasında değer giriniz")

else:
    print("Üzgünüm yanlış tahmin!")
    print("Doğru cevap 6 idi.")

# Kullanıcıya 3 farklı kelime sorup tahmin ettiğimiz kelimeyi bulmasını isteyelim. Ekran çıktılarını if-elif-else ile yazıralım.


"""kelime1="kedi"

tahmin=input("tahmin edin: ")

if tahmin==kelime1:
    print("Tebrikler doğru tahmin!")

elif tahmin=="köpek":
    print("Yanlış tahmin, düşmanınını tahmin ettiniz:)")

else: print("Üzgünüm yanlış tahmin!")"""


