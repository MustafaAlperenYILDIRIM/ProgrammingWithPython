# TRY-EXCEPT SÖZ DİZİMİ

try:
    x=int(input("Bir sayı giriniz:"))
    y=int(input("Bir sayı daha giriniz:")) 

except ValueError:
    print("Lütfen geçerli sayı giriniz.")

except ZeroDivisionError:
    print("Sıfıra bölme hatası.")

else:
    print("Girilen iki sayının bölümü:",x/y)  

finally:
    print("Program bitti.")
    

################ RAISE ###############

yas=int(input("Yaşınızı giriniz:"))

if yas<18:
    raise ValueError("Yaşınız 18'den küçükse girişe izin verilmez.")
print("Yaşınız",yas)

################ EXCEPTION ###############

class OzelHata(Exception):
    pass

try:
    raise OzelHata("Bu özel bir hatadır.")

except OzelHata as e:
    print("Ozel Hata:",e)