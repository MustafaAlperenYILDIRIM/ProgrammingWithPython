def switch(yil):
    if yil==1:
        print("Mühendis")

    elif yil==2:
        print("Uzman Mühendis")

    elif yil==3:
        print("Kıdemli Uzman")

    else: print("9'dan büyük değer girdiniz")

try:
   
    yil = int(input("""0-3 yıl tecrübe için 1,
3-6 yıl tecrübe için 2,
6-9 yıl tecrübe için 3,
sayıyı giriniz: """))
    switch(yil)
    

except ValueError:
    print("Değer tipi hatası, lütfen geçerli bir sayı giriniz!")