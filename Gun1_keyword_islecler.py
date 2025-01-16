"""import keyword
print(keyword.kwlist)

ders_adi,sure,pi,python_egitimi_mi="Python Temel Eğitmi",5,3.14,True

print(type(ders_adi))
print(type(sure))
print(type(pi))
print(type(python_egitimi_mi))"""

#Aritmetik İşleçler
"""
x=81
y=6
toplam=0

toplam=x+y
print("x+y=",toplam,"\n")#87

toplam=x-y
print("x-y=",toplam,"\n")#75

toplam=x*y
print("x*y=",toplam,"\n")#486

toplam=x/y
print("x/y=",toplam,"\n")

toplam=x**y
print("x^y=",toplam,"\n")

toplam=x%y
print("x%y=",81%6,"\n")#3

if((x>1)and(y<7)):
    print("koşul geçerli")

else:print("koşul geçersiz")"""

"""#sayıyı gir
a=int(input("0-9 arası sayıyı tahmin ediniz:"))
#int() yazılmallıdır çünkü input fonksiyonu str değer döndürür

#tahmin edilen sayıyı bulduydsa ekrana yazdır
if a==8:
    print("8 sayısını buldunuz")

elif a==7:
    print("Sayıya çok yaklaştınız")

elif a==9:
    print("Sayıya çok yaklaştınız")

else:
    print("Sayıyı bulamadınız")
"""
"""a=input("ilk sayıyı giriniz:")
a=int(a)
b=input("ikinci sayıyı giriniz:")
b=int(b)
c=input("üçüncü sayıyı giriniz:")
c=int(c)
if a<b:
    if a<c:
        print("En Küçük Sayı:", a)
    else:
        print("En Küçük Sayı:", c)
elif b<c:
    print("En Küçük Sayı:", b)
else:
    print("En Küçük Sayı:", c)"""



"""def switch(deger):
    case={}
    while True:
        try:
            case={
                0:"case 0",
                1:"case 1",
                2:"case 2",
                "default":"hatalı giriş"
            }

            print(case[deger])
            break

        except KeyError:
            print(case["default"])
            break

deger=input("case seçiniz(0-1-2):")"""

miktar=int(input("yazdırılacak doğal sayı miktarı:"))
i=0
while i<=miktar:
    print("{}.sayı:{}".format(i+1,i))
    i+=1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)