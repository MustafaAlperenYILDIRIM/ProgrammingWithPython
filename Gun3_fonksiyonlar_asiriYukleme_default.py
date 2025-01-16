def carpma(x,y=1,z=1):
    return x*y*z

print(carpma(2))
print(carpma(2,3))
print(carpma(2,3,4))


#docstring ve aşırı yükleme özelliklerini kullanalım
#kullanıcı adı-soyadı-yaşı değerlerini dinamik olarak bir program yazalım
#eksik veri girişi yapıldığında soyisim veya yaş için ***** yazdıralım 
#fonksiyonAdi.__doc__ metodunu kullanarak ekrana fonksiyon hakkında bilgi yazdıralım

#bitiş süresi 11.05

def kullaniciBilgileri(x,y,z):
    """
    Kullanıcı Bilgilerini Alır.

    değişkenler:
    x (str): Kullanıcı Adı
    y (str): Kullanıcı Soyadı
    z (int): Kullanıcı Yaşı

    çıktı:
    Kullanıcı Bilgileri

    """

    if x=="":
        x="***"

    if y=="":
        y="***"
       
    if z=="":
        z="***" 

    print(f"ad:{x}, soyad:{y}, yaş:{z}")

ad=input("isminizi giriniz:")
soyad=input("soy isminizi giriniz:")
yas=input("yaşınızı giriniz:")




kullaniciBilgileri(ad,soyad,yas)
#print(kullaniciBilgileri.__doc__)